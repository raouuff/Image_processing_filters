import numpy as np
def bilinear_interpolation(input_image, new_width, new_height):
    # Ensure the input image is a NumPy array
    input_image = np.array(input_image)
    
    # Get the dimensions of the input image
    old_height, old_width = input_image.shape
    
    # Create an empty output image
    output_image = np.zeros((new_height, new_width), dtype=np.float32)
    
    # Calculate the scale factors
    x_scale = (old_width - 1) / (new_width - 1)
    y_scale = (old_height - 1) / (new_height - 1)
    
    # Perform bilinear interpolation
    for new_y in range(new_height):
        for new_x in range(new_width):
            x = new_x * x_scale
            y = new_y * y_scale
            x1 = int(x)
            y1 = int(y)
            x2 = min(x1 + 1, old_width - 1)
            y2 = min(y1 + 1, old_height - 1)
            dx = x - x1
            dy = y - y1
            pixel_value = (
                input_image[y1, x1] * (1 - dx) * (1 - dy) +
                input_image[y1, x2] * dx * (1 - dy) +
                input_image[y2, x1] * (1 - dx) * dy +
                input_image[y2, x2] * dx * dy
            )
            output_image[new_y, new_x] = pixel_value
    
    # Normalize the output image to ensure pixel values are in the correct range (0-255)
    output_image = np.clip(output_image, 0, 255).astype(np.uint8)
    
    return output_image