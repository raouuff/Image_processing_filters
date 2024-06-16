import matplotlib.pyplot as plt
import numpy as np
import cv2

def equalizeHistogram(img):
    img_height, img_width = img.shape
    # Calculate histogram
    histogram = np.zeros(256, np.int32)
    img = img.astype(int)
    for i in range(img_height):
        for j in range(img_width):
            pixel_value = img[i, j]
            histogram[pixel_value] += 1
    #calcualte pdf 
    total_pixels = img_height * img_width
    pdf_img = histogram / total_pixels
    # Plot original image and its histogram
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    #ploting
    plt.subplot(2, 2, 2)
    plt.bar(range(256), histogram, color='b', alpha=0.7)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Original Histogram')

    # Calculate CDF
    cdf = np.zeros([256], float)
    cdf[0] = pdf_img[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + pdf_img[i]
    
    # Number of intensity levels
    L = 256
    # Compute Transformation Function T(x)
    cdf_eq = np.round((cdf * (L - 1)), 0).astype(np.uint8)
    
    # Create equalized image
    imgEqualized = np.zeros((img_height, img_width), dtype=np.uint8)
    for i in range(img_height):
        for j in range(img_width):
            r = img[i, j]
            s = cdf_eq[r]
            imgEqualized[i, j] = s
    
    # Calculate histogram of equalized image
    histogram_eq = np.zeros(256, np.int32)
    for i in range(img_height):
        for j in range(img_width):
            pixel_value = imgEqualized[i, j]
            histogram_eq[pixel_value] += 1

    # Plot equalized image and its histogram
    plt.subplot(2, 2, 3)
    plt.imshow(imgEqualized, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.bar(range(256), histogram_eq, color='r', alpha=0.7)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Equalized Histogram')

    plt.tight_layout()
    plt.show()

    return imgEqualized


