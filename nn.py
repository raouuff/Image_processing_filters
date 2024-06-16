import numpy as np
def nn(img, m, n):
    x, y = img.shape
    new_img = np.zeros((m, n), dtype=img.dtype)
    row_ratio = x / m
    col_ratio = y / n
    for i in range(m):
        for j in range(n):
            xn = int(i * row_ratio)
            yn = int(j * col_ratio)
            new_img[i, j] = img[min(xn, x - 1), min(yn, y - 1)]
    return new_img
