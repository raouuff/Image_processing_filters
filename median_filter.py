
import cv2
import numpy as np
from matplotlib import pyplot as pit
import math
import matplotlib.pyplot as plt

def apply_median_filter(image):
    filtered_image = np.zeros(image.shape, dtype=np.uint8)
    height, width = image.shape
    for i in range(1, height-1 ):
        for j in range(1, width-1 ):
            neighborhood = image[i-1:i+2, j-1:j+2]

            sorted_pixels = np.sort(neighborhood.flatten())

            median_value = sorted_pixels[len(sorted_pixels) // 2]

            filtered_image[i, j] = median_value

    return filtered_image
