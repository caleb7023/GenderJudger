#!/usr/bin/env python3

# Author: caleb7023

import cupy as cp

import os

import cv2

NeuronWeights = cp.load("Data/NeuronWeights.npy")


# Train the AI
def Train(Dir : str, Man : bool):

    global NeuronWeights

    Img = cp.load(Dir)

    if False: # Debug mode
        cv2.imshow("debug", cp.uint8(Img.get()))
        cv2.imshow("debug2", cp.uint8(NeuronWeights.get()))
        cv2.waitKey(1)

    if (0 < cp.sum(Img * NeuronWeights)) != Man:
        if Man: NeuronWeights += Img
        else  : NeuronWeights -= Img
        return 1
    return 0


def main():
    ManFileCount   = len(os.listdir("Data/man"))
    WomanFileCount = len(os.listdir("Data/woman"))

    global NeuronWeights

    with open("Data/Terms"     , "r") as f: Terms      = int(f.read())
    with open("Data/TotalFails", "r") as f: TotalFails = int(f.read())

    while 1:

        Fails = 0

        for i in range(10000):
            Fails += Train(f"Data/man/{Terms % ManFileCount}.npy"    , True)
            Fails += Train(f"Data/woman/{Terms % WomanFileCount}.npy", False)
            Terms += 2
        
        TotalFails += Fails

        with open("Data/Terms"     , "w") as f: f.write(str(Terms))
        with open("Data/TotalFails", "w") as f: f.write(str(TotalFails))

        cp.save("Data/NeuronWeights", NeuronWeights)
        print(f"Total terms:{Terms}, Total fails:{TotalFails}, Fails:{Fails}/20000")




if __name__ == "__main__":
    main()