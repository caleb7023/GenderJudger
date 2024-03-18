#!/usr/bin/env python3

# Author: caleb7023

import cv2

import cupy as cp

# Set up camera
CAMERA = cv2.VideoCapture(0)
# Set the size to 100x100 for when camera captures
CAMERA.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
CAMERA.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

# Load the neuron weights for judging the gender from the img
NEURON_WEIGHTS = cp.load("./TrainData/NeuronWeights.npy")

def JudgeGender(Img) -> bool:
    # True means the img is a img of a man face
    return True if 0 < cp.sum(NEURON_WEIGHTS * Img) else False


def main():

    while 1:

        # Get img from the camera
        Frame = CAMERA.read()

        Result = cv2.putText(Frame[1], "MAN" if JudgeGender(Frame[1]) else "WOMAN", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, "White", 2, cv2.LINE_AA)

        # Show the result
        cv2.imshow("Camera", Result)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()