import cv2
import random
import numpy as np
import matplotlib.pyplot as plt
def add_uniform_noise(image, noise_min=0, noise_max=30):
    rows, cols = image.shape
    # Create an empty image for noisy output
    noisy_image = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            # Generate uniform noise manually
            noise =  np.random.uniform(noise_min , noise_max)
            # Add the noise to the pixel value
            noisy_pixel = image[i, j] + noise
            # Clip the pixel value to ensure it remains within the valid range [0, 255]
            noisy_pixel = max(0, min(255, noisy_pixel))
            # Store the noisy pixel value in the noisy image
            if noisy_pixel>255:
                noisy_pixel= 255
            elif noisy_pixel < 0 :
                noisy_pixel=0
            noisy_image[i][j] = int(noisy_pixel)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title('Noisy Image')
    plt.imshow(noisy_image, cmap='gray')
    plt.axis('off')
    plt.show()
    return noisy_image