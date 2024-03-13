import os
import cv2
import numpy as np

def main():
    for index, dir in os.listdir("man/"):
        Img = cv2.imread(f"man/{dir}")
        np.save(f"Data/Man/{index}", Img)

    for index, dir in os.listdir("woman/"):
        Img = cv2.imread(f"woman/{dir}")
        np.save(f"Data/Woman/{index}", Img)


if __name__ == "__main__":
    main()