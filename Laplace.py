import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d
def Laplace(img):
    def gaussian_kernel(size, sigma=1):
        size = int(size) // 2
        x, y = np.mgrid[-size:size+1, -size:size+1]
        normal = 1 / (2.0 * np.pi * sigma**2)
        g = np.exp(-((x**2 + y**2) / (2.0 * sigma**2))) * normal
        return g

    def apply_laplacian(image):
        laplacian_kernel = np.array([[0, -1, 0],
                                    [-1, 4, -1],
                                    [0, -1, 0]])
        laplacian_kernel = laplacian_kernel / np.sum(np.abs(laplacian_kernel))
        return convolve2d(image, laplacian_kernel, mode='same')
    
    image = np.array(img)
    gaussian = gaussian_kernel(5, sigma=1)
    blurred = convolve2d(image, gaussian, mode='same', boundary='wrap')

    laplacian = apply_laplacian(blurred)

    sharpened = image + laplacian

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('blurred')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(sharpened, cmap='gray')
    plt.title('Sharpened')
    plt.axis('off')


    plt.tight_layout()
    plt.show()
