import numpy as np 
def apply_Gaussian_filter(image):
    height, width = image.shape
    Gkernel = np.array([[1, 2, 1],
                    [2, 4, 2],
                    [1, 2, 1]], dtype=np.float64)
    Gkernel=Gkernel/16
    filtered_image = np.zeros(image.shape, dtype=np.float64)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Extract the 3x3 neighborhood
            neighborhood = image[i - 1:i + 2, j - 1:j + 2]
            # Compute the mean value of the neighborhood
            Gaussian_value=np.sum(Gkernel*neighborhood)
            # Assign the mean value to the corresponding pixel
            filtered_image[i, j] = Gaussian_value
    filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
    return filtered_image
