import numpy as np

def apply_averaging_filter(image):
    height, width = image.shape
    filtered_image = np.zeros(image.shape, dtype=np.uint8)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            neighborhood = image[i - 1:i + 2, j - 1:j + 2]
            mean_value = np.mean(neighborhood)
            filtered_image[i, j] = mean_value

    return filtered_image
