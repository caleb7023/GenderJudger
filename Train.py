#!/usr/bin/env python3

# Author: caleb7023

import cupy as cp    # For training
import os            # To get the list of the data files
if False: import cv2 # For debugging

# Load the neuron weights
NeuronWeights = cp.load("Data/NeuronWeights.npy")

# Train the AI
def Train(Dir : str, Man : bool):

    global NeuronWeights

    # Load the img to train the AI
    Img = cp.load(Dir)

    if False: # Debug mode
        cv2.imshow("debug", cp.uint8(Img.get())) # show the loaded img
        cv2.imshow("debug2", cp.uint8(NeuronWeights.get())) # show the neuron weights
        cv2.waitKey(1)

    # Check the gender prediction is right or not.
    # If prediction wasnt right -> Modify the neuron weights.
    # If prediction was right -> Do nothin.
    if (0 < cp.sum(Img * NeuronWeights)) != Man:
        if Man: NeuronWeights += Img
        else  : NeuronWeights -= Img
        return 1
    return 0


def main():

    # Count how much file is in the man and woman face data directory.
    ManFileCount   = len(os.listdir("Data/man"))
    WomanFileCount = len(os.listdir("Data/woman"))

    global NeuronWeights

    # load the last terms and total fials.
    with open("Data/Terms"     , "r") as f: Terms      = int(f.read())
    with open("Data/TotalFails", "r") as f: TotalFails = int(f.read())

    while 1:

        Fails = 0

        for i in range(10000):
            Fails += Train(f"Data/man/{int(Terms*.5 % ManFileCount)}.npy"    , True)
            Fails += Train(f"Data/woman/{int(Terms*.5 % WomanFileCount)}.npy", False)
            Terms += 2
        
        TotalFails += Fails

        # save the neuron weights, terms and total fails.
        with open("Data/Terms"     , "w") as f: f.write(str(Terms))
        with open("Data/TotalFails", "w") as f: f.write(str(TotalFails))
        cp.save("Data/NeuronWeights", NeuronWeights)

        # Print the data to console to check train progress
        print(f"Total terms:{Terms}, Total fails:{TotalFails}, Fails:{Fails}/20000")


if __name__ == "__main__":
    main()