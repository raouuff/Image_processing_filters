import cv2
import numpy as np
import matplotlib.pyplot as plt
def Roberts_Cross_Gradient(img):

    roberts_cross_v = np.array([[1, 0], [0, -1]])
    roberts_cross_h = np.array([[0, 1], [-1, 0]])
    
    # img = cv2.imread("/content/Real Madrid.jpg", 0).astype('float64')
    img /= 255.0

    vertical = convolve(img, roberts_cross_v)
    horizontal = convolve(img, roberts_cross_h)

    edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
    edged_img *= 255
    edged_img = edged_img.astype('uint8')

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Edge-detected Image')
    plt.imshow(edged_img, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
def convolve(image, kernel):
        image_height, image_width = image.shape
        kernel_height, kernel_width = kernel.shape
        pad_height = kernel_height // 2
        pad_width = kernel_width // 2

        padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
        output = np.zeros_like(image)

        for i in range(image_height):
            for j in range(image_width):
                region = padded_image[i:i + kernel_height, j:j + kernel_width]
                output[i, j] = np.sum(region * kernel)

        return output
