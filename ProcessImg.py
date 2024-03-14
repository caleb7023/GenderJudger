#!/usr/bin/env python3

# Author: caleb7023

import os
import cv2
import numpy as np

# Create the Man/Woman directory in ./Data directory to save processed img
# If the directory exists, its gonna be passed.
try: Path = os.path.join("./"    , "Data" ); os.mkdir(Path)
except: pass
try: Path = os.path.join("./Data", "man"  ); os.mkdir(Path)
except: pass
try: Path = os.path.join("./Data", "woman"); os.mkdir(Path)
except: pass


def main():
    ProccesImg(True)  # Process man imgs
    ProccesImg(False) # Process woman imgs


def ProccesImg(Man: bool):

    Directory: str = ["woman", "man"][Man] # Img directory name in the archive/faces directory

    # Load every single img in the gender directory and convert the JPG file to numpy array file
    for index, dir in enumerate(os.listdir(f"./archive/faces/{Directory}/")):

        # Load the img
        Img = cv2.imread(f"./archive/faces/{Directory}/{dir}")

        # Resize the img to 100x100 array
        Img = cv2.resize(Img, (100, 100))

        # Save the array to ./Data/Man directory or ./Data/Woman
        Img = np.save(f"./Data/{Directory}/{index}", Img)


if __name__ == "__main__":
    main()

