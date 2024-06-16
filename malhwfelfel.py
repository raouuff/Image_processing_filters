import cv2
import random
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, salt_prob=0.05, pepper_prob=0.05):
    noisy_image = image.copy()
    total_pixels = image.size
    num_salt = int(salt_prob * total_pixels )
    num_pepper = int(pepper_prob * total_pixels )

    # Add Salt noise
    for _ in range(num_salt):
        y = random.randint(0, image.shape[0] - 1)
        x = random.randint(0, image.shape[1] - 1)
        noisy_image[y, x] = 255

    # Add Pepper noise
    for _ in range(num_pepper):
        y = random.randint(0, image.shape[0] - 1)
        x = random.randint(0, image.shape[1] - 1)
        noisy_image[y, x] = 0
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
