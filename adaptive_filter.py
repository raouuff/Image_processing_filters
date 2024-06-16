import cv2
import numpy as np
from matplotlib import pyplot as pit
import math
import matplotlib.pyplot as plt
from median_filter import apply_median_filter
def AdaptiveFilters(image,mode):
    if mode=="Min":
        return Minfilter(image)
    elif mode =="Max":
        return Maxfilter(image)
    elif mode=="Median":
        return apply_median_filter(image)

def Minfilter(image):
    height, width = image.shape
    filtered_image = np.zeros(image.shape, dtype=np.uint8)
    for i in range(1, height-1 ):
        for j in range(1, width -1):
            neighborhood = image[i-1:i+2, j-1:j+2]
            min_value = np.min(neighborhood)
            filtered_image[i, j] = min_value
    return filtered_image
def Maxfilter(image):
    height, width = image.shape
    filtered_image = np.zeros(image.shape, dtype=np.uint8)
    for i in range(1, height-1 ):
        for j in range(1, width-1):
            neighborhood = image[i-1:i+2, j-1:j+2]

            max_value = np.max(neighborhood)

            filtered_image[i, j] = max_value

    return filtered_image