import cv2
import numpy as np
import matplotlib.pyplot as plt
def Unsharp_Mask(img):
    blurred_img = cv2.GaussianBlur(src=img, ksize=(31,31), sigmaX=0, sigmaY=0)

# Extract mask
    mask = img - blurred_img

# Lw el k > 1 hyb2a highboost filtering bn enhancing the edges
    k = 1
    highboost = img + k * mask

    plt.imshow(highboost, cmap='gray')
    plt.axis('off')
    plt.show()

    # To Add blur manualy
# def gaussian_kernel(size, sigma):
#     """
#     Generates a 2D Gaussian kernel.
#     Args:
#         size (int): Size of the kernel (odd number).
#         sigma (float): Standard deviation for Gaussian distribution.
#     Returns:
#         np.ndarray: 2D Gaussian kernel.
#     """
#     kernel = np.zeros((size, size))
#     center = size // 2
#     for i in range(size):
#         for j in range(size):
#             x, y = i - center, j - center
#             kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
#     return kernel / (2 * np.pi * sigma**2)

# def apply_gaussian_blur(image, kernel_size, sigma):
#     """
#     Applies Gaussian blur to the input image.
#     Args:
#         image (np.ndarray): Input grayscale image.
#         kernel_size (int): Size of the Gaussian kernel (odd number).
#         sigma (float): Standard deviation for Gaussian distribution.
#     Returns:
#         np.ndarray: Blurred image.
#     """
#     kernel = gaussian_kernel(kernel_size, sigma)
#     blurred_image = cv2.filter2D(image, -1, kernel)
#     return blurred_image



# # Apply Gaussian blur
# kernel_size = 9
# sigma = 3
# blurred_img = apply_gaussian_blur(img, kernel_size, sigma)

# Blur the image
