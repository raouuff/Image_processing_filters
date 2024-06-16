from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import cv2
def Sobel(img):
    Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
    Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
    [rows, columns] = np.shape(img)
    sobel_filtered_image = np.zeros(shape=(rows, columns))
    for i in range(rows - 2):
        for j in range(columns - 2):
            gx = np.sum(np.multiply(Gx, img[i:i + 3, j:j + 3]))
            gy = np.sum(np.multiply(Gy, img[i:i + 3, j:j + 3]))
            sobel_filtered_image[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2)
    fig2 = plt.figure(2)
    ax1, ax2 = fig2.add_subplot(121), fig2.add_subplot(122)
    ax1.imshow(img, cmap=plt.get_cmap('gray'))
    ax2.imshow(sobel_filtered_image, cmap=plt.get_cmap('gray'))
    fig2.show()
