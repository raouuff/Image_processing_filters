import numpy as np
from histogramEq import equalizeHistogram
import matplotlib.pyplot as plt

def histogram_specification(source_img, reference_img):
    # Equalize both source and reference images
    equalized_source_img = equalizeHistogram(source_img)
    equalized_reference_img = equalizeHistogram(reference_img)
    
    source_height, source_width = equalized_source_img.shape
    ref_height, ref_width = equalized_reference_img.shape
    
    # Calculate histograms for both images
    source_hist = np.zeros(256, np.int32)
    ref_hist = np.zeros(256, np.int32)
    
    for i in range(source_height):
        for j in range(source_width):
            source_hist[equalized_source_img[i, j]] += 1
    
    for i in range(ref_height):
        for j in range(ref_width):
            ref_hist[equalized_reference_img[i, j]] += 1
    
    # Calculate CDFs for both images
    source_cdf = np.zeros(256, np.float32)
    ref_cdf = np.zeros(256, np.float32)
    
    sum_hist = 0
    total_source_pixels = source_height * source_width
    for i in range(256):
        sum_hist += source_hist[i]
        source_cdf[i] = sum_hist / total_source_pixels
    
    sum_hist = 0
    total_ref_pixels = ref_height * ref_width
    for i in range(256):
        sum_hist += ref_hist[i]
        ref_cdf[i] = sum_hist / total_ref_pixels
    
    
    # Create a mapping from source image to reference image
    mapping = np.zeros(256, dtype=np.uint8)
    ref_index = 0
    for src_index in range(256):
        while ref_index < 256 and ref_cdf[ref_index] < source_cdf[src_index]:
            ref_index += 1
        mapping[src_index] = ref_index if ref_index < 256 else 255
    
    # Apply the mapping to the source image
    matched_img = np.zeros_like(equalized_source_img)
    for i in range(source_height):
        for j in range(source_width):
            matched_img[i, j] = mapping[equalized_source_img[i, j]]
    
    # Calculate histogram of matched image
    matched_hist = np.zeros(256, np.int32)
    for i in range(source_height):
        for j in range(source_width):
            matched_hist[matched_img[i, j]] += 1
    
    # Plot original, reference, and matched images with their histograms
    plt.figure(figsize=(18, 12))
    
    plt.subplot(3, 2, 1)
    plt.imshow(source_img, cmap='gray')
    plt.title('Source Image')
    plt.axis('off')
    
    plt.subplot(3, 2, 2)
    plt.bar(range(256), source_hist, color='b', alpha=0.7)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Source Histogram')
    
    plt.subplot(3, 2, 3)
    plt.imshow(reference_img, cmap='gray')
    plt.title('Reference Image')
    plt.axis('off')
    
    plt.subplot(3, 2, 4)
    plt.bar(range(256), ref_hist, color='g', alpha=0.7)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Reference Histogram')
    
    plt.subplot(3, 2, 5)
    plt.imshow(matched_img, cmap='gray')
    plt.title('Matched Image')
    plt.axis('off')
    
    plt.subplot(3, 2, 6)
    plt.bar(range(256), matched_hist, color='r', alpha=0.7)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Matched Histogram')
    
    plt.tight_layout()
    plt.show()
    
    return matched_img