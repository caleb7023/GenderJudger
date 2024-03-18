#!/usr/bin/env python3

# Author: caleb7023

import os            # To get the list of the data files
import numpy as np   # For training
import time
if False: import cv2 # For debugging


# Train the AI
def Train(Data, Man : bool):

    global NeuronWeights

    if False: # Debug mode
        cv2.imshow("debug", np.uint8(Img).get()) # show the loaded img
        cv2.imshow("debug2", np.uint8(NeuronWeights).get()) # show the neuron weights
        cv2.waitKey(1)

    # Check the gender prediction is right or not.
    # If prediction wasnt right -> Modify the neuron weights.
    # If prediction was right -> Do nothin.
    if (0 < np.sum(Data * NeuronWeights)) != Man:
        if Man: NeuronWeights += Data
        else  : NeuronWeights -= Data
        return 1
    return 0


def main():

    global FailList

    # load the last terms and total fials.
    with open("./TrainData/Terms"     , "r") as f: Terms      = int(f.read())
    with open("./TrainData/TotalFails", "r") as f: TotalFails = int(f.read())

    while 1:

        Fails = 0

        StartTime = time.time()

        for i in range(50000):
            Fails += Train(Datas[0][int(Terms*.5 %  ManFileCount )], True)
            Fails += Train(Datas[1][int(Terms*.5 % WomanFileCount)], False)
            Terms += 2
        
        TotalFails += Fails
        FailList = np.append(FailList, Fails)

        # Print the data to console to check train progress
        EndTime = time.time()
        ElapsedTime = EndTime - StartTime
        print(f"Total terms:{Terms}, Total fails:{TotalFails}, Fails:{Fails}/100000, Elapsed time:{round(ElapsedTime, 3)}")

        # save the neuron weights, terms and total fails.
        with open("./TrainData/Terms"     , "w") as f: f.write(str(Terms))
        with open("./TrainData/TotalFails", "w") as f: f.write(str(TotalFails))
        np.save("./TrainData/NeuronWeights", NeuronWeights)
        np.save("./TrainData/FailList"     , FailList)



def LoadDatas():

    global Datas

    for i in range( ManFileCount ): Datas[0] += [np.load( f"./Data/man/{i}.npy" )]
    for i in range(WomanFileCount): Datas[1] += [np.load(f"./Data/woman/{i}.npy")]


if __name__ == "__main__":

    # Load the neuron weights and TrainData fail list
    NeuronWeights = np.load("./TrainData/NeuronWeights.npy")
    FailList      = np.load("./TrainData/FailList.npy"     )
    
    # Count how much file is in the man and woman face data directory.
    ManFileCount   = len(os.listdir("./Data/man"  ))
    WomanFileCount = len(os.listdir("./Data/woman"))

    Datas = [[], []]

    LoadDatas()

    main()