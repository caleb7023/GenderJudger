#!/usr/bin/env python3

# Author: caleb7023

import numpy as cp   # For loading
import os            # To get the list of the data files
import time
if False: import cv2 # For debugging

# Load the neuron weights
NeuronWeights = cp.load("Data/NeuronWeights.npy")

# Train the AI
def Train(Data, Man : bool):

    global NeuronWeights

    if False: # Debug mode
        cv2.imshow("debug", cp.uint8(Img).get()) # show the loaded img
        cv2.imshow("debug2", cp.uint8(NeuronWeights).get()) # show the neuron weights
        cv2.waitKey(1)

    # Check the gender prediction is right or not.
    # If prediction wasnt right -> Modify the neuron weights.
    # If prediction was right -> Do nothin.
    if (0 < cp.sum(Data * NeuronWeights)) != Man:
        if Man: NeuronWeights += Data
        else  : NeuronWeights -= Data
        return 1
    return 0


def main():

    global NeuronWeights

    # load the last terms and total fials.
    with open("Data/Terms"     , "r") as f: Terms      = int(f.read())
    with open("Data/TotalFails", "r") as f: TotalFails = int(f.read())

    while 1:

        Fails = 0

        StartTime = time.time()

        for i in range(20000):
            Fails += Train(Datas[0][int(Terms*.5 %  ManFileCount )], True)
            Fails += Train(Datas[1][int(Terms*.5 % WomanFileCount)], False)
            Terms += 2
        
        TotalFails += Fails

        # save the neuron weights, terms and total fails.
        with open("Data/Terms"     , "w") as f: f.write(str(Terms))
        with open("Data/TotalFails", "w") as f: f.write(str(TotalFails))
        cp.save("Data/NeuronWeights", NeuronWeights)

        # Print the data to console to check train progress
        print(f"Total terms:{Terms}, Total fails:{TotalFails}, Fails:{Fails}/40000, Time:{round(time.time() - StartTime, 3)}")


def LoadDatas():

    global Datas

    for i in range( ManFileCount ): Datas[0] += [cp.load( f"./Data/man/{i}.npy" )]
    for i in range(WomanFileCount): Datas[1] += [cp.load(f"./Data/woman/{i}.npy")]

if __name__ == "__main__":
    
    # Count how much file is in the man and woman face data directory.
    ManFileCount   = len(os.listdir("./Data/man"))
    WomanFileCount = len(os.listdir("./Data/woman"))

    Datas = [[], []]

    LoadDatas()

    main()