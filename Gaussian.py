import cv2
import random
import math
import matplotlib.pyplot as plt
import numpy as np

def box_muller_transform():
    # Generate two uniform random numbers in (0, 1)
    u1 = random.random()
    u2 = random.random()
    # Perform Box-Muller transform
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    return z0
def add_gaussian_noise(image, mean=0, std_dev=25):
    rows, cols = image.shape
    # Create an empty image for noisy output
    noisy_image = np.zeros_like(image, dtype=np.float32)

    for i in range(rows):
        for j in range(cols):
            # Generate Gaussian noise
            noise = box_muller_transform() * std_dev + mean
            # Add the noise to the pixel value
            noisy_pixel = image[i, j] + noise
            # Clip the pixel value to be between 0 and 255
            if noisy_pixel > 255:
                noisy_pixel = 255
            elif noisy_pixel < 0:
                noisy_pixel = 0
            # Store the noisy pixel value in the noisy image
            
            noisy_image[i, j] = int(noisy_pixel)

    # Convert the noisy image to uint8
    
    # Plot the original and noisy images using Matplotlib
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