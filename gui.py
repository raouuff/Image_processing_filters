import tkinter as tk
from tkinter import filedialog, ttk,messagebox
from PIL import ImageTk, Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from median_filter import apply_median_filter
from adaptive_filter import AdaptiveFilters
from histogramEq import equalizeHistogram
from Roberts_Cross_Gradient_Operators import Roberts_Cross_Gradient
from Laplace import Laplace
from sobel_Operators import Sobel
from UnsharpMask import Unsharp_Mask
from malhwfelfel import add_salt_and_pepper_noise
from Gaussian import add_gaussian_noise
from uniform_noise import add_uniform_noise
from Histogram_Specification import histogram_specification
from avaregefilter import apply_averaging_filter
from GaussianFilter import apply_Gaussian_filter
from Fourier import fourier_transform, fourier_inverse
from nn import nn
from bilinear import bilinear_interpolation
from hoffman import compress_image_with_huffman
image_path = ""
reference_image_path = ""
adaptive_option_var = None  # Declare global variable
def open_image():
    global image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image_path = file_path
        image = image.resize((400, 400))
        tk_image = ImageTk.PhotoImage(image)
        label.config(image=tk_image)
        label.image = tk_image

def open_reference_image():
    global reference_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image = Image.open(file_path)
        reference_image_path = file_path
        image = image.resize((400, 400))
        tk_image = ImageTk.PhotoImage(image)
        ref_label.config(image=tk_image)
        ref_label.image = tk_image

def on_dropdown_change(event):
    global adaptive_option_var, ref_button, mean_entry, std_dev_entry, mean_label, std_dev_label
    global salt_prob_entry, pepper_prob_entry, salt_prob_label, pepper_prob_label
    global noise_min_entry, noise_max_entry, noise_min_label, noise_max_label
    global new_width_entry, new_height_entry, new_width_label, new_height_label

    selected_operation = dropdown.get()

    for widget in filter_frame.winfo_children():
        widget.destroy()

    if selected_operation == "Adaptive filter":
        adaptive_options = ["Max", "Min", "Median"]
        adaptive_option_var.set("None")
        for i, option in enumerate(adaptive_options):
            radio_button = tk.Radiobutton(filter_frame, text=option, variable=adaptive_option_var, value=option)
            radio_button.pack(anchor=tk.W)
    
    if selected_operation == "Histogram Specification":
        ref_button.pack()
    
    if selected_operation == "Gaussian noise":
        mean_label = tk.Label(filter_frame, text="Mean:")
        mean_label.pack(anchor=tk.W)
        mean_entry = tk.Entry(filter_frame)
        mean_entry.pack(anchor=tk.W)

        std_dev_label = tk.Label(filter_frame, text="Std Dev:")
        std_dev_label.pack(anchor=tk.W)
        std_dev_entry = tk.Entry(filter_frame)
        std_dev_entry.pack(anchor=tk.W)
    
    if selected_operation == "Impulse noise":
        salt_prob_label = tk.Label(filter_frame, text="Salt Probability:")
        salt_prob_label.pack(anchor=tk.W)
        salt_prob_entry = tk.Entry(filter_frame)
        salt_prob_entry.pack(anchor=tk.W)

        pepper_prob_label = tk.Label(filter_frame, text="Pepper Probability:")
        pepper_prob_label.pack(anchor=tk.W)
        pepper_prob_entry = tk.Entry(filter_frame)
        pepper_prob_entry.pack(anchor=tk.W)
    
    if selected_operation == "Uniform noise":
        noise_min_label = tk.Label(filter_frame, text="Noise Min:")
        noise_min_label.pack(anchor=tk.W)
        noise_min_entry = tk.Entry(filter_frame)
        noise_min_entry.pack(anchor=tk.W)

        noise_max_label = tk.Label(filter_frame, text="Noise Max:")
        noise_max_label.pack(anchor=tk.W)
        noise_max_entry = tk.Entry(filter_frame)
        noise_max_entry.pack(anchor=tk.W)

    if selected_operation == "bilinear" or selected_operation == "nearest neighbor":
        new_width_label = tk.Label(filter_frame, text="New Width:")
        new_width_label.pack(anchor=tk.W)
        new_width_entry = tk.Entry(filter_frame)
        new_width_entry.pack(anchor=tk.W)

        new_height_label = tk.Label(filter_frame, text="New Height:")
        new_height_label.pack(anchor=tk.W)
        new_height_entry = tk.Entry(filter_frame)
        new_height_entry.pack(anchor=tk.W)


def run_operation():
    global image_path, reference_image_path, adaptive_option_var
    selected_operation = dropdown.get()
    image = cv2.imread(image_path, 0).astype('float64')
    imageInt = cv2.imread(image_path, 0)
    ref_image = cv2.imread(reference_image_path, 0)
    if selected_operation == "Median filter":
        processed_image = apply_median_filter(image)
    elif selected_operation == "Adaptive filter":
        adaptive_option_value = adaptive_option_var.get()
        if adaptive_option_value:
            processed_image = AdaptiveFilters(image, adaptive_option_value)
    elif selected_operation == "Histogram Equalization":
        processed_image= equalizeHistogram(imageInt)
    elif selected_operation == 'Roberts Cross-Gradient Operators':
        processed_image = Roberts_Cross_Gradient(image)
    elif selected_operation == "Laplacian Operator":
        processed_image = Laplace(image)
    elif selected_operation == "Sobel Operators":
        processed_image = Sobel(image)
    elif selected_operation == "Unsharp Masking and Highboost Filtering":
        processed_image = Unsharp_Mask(image)
    elif selected_operation == "Impulse noise":
        try:
            salt_prob = float(salt_prob_entry.get())
            pepper_prob = float(pepper_prob_entry.get())
            processed_image = add_salt_and_pepper_noise(imageInt, salt_prob, pepper_prob)
        except ValueError:
            print("Please enter valid numbers for salt and pepper probabilities.")
    elif selected_operation == "Gaussian noise":
        try:
            mean = float(mean_entry.get())
            std_dev = float(std_dev_entry.get())
            processed_image = add_gaussian_noise(imageInt, mean, std_dev)
        except ValueError:
            print("Please enter valid numbers for mean and standard deviation.")
    elif selected_operation == "Uniform noise":
        try:
            noise_min = float(noise_min_entry.get())
            noise_max = float(noise_max_entry.get())
            processed_image = add_uniform_noise(imageInt, noise_min, noise_max)
        except ValueError:
            print("Please enter valid numbers for noise min and max.")
    elif selected_operation == "Histogram Specification":
        if reference_image_path:
            processed_image = histogram_specification(imageInt, ref_image)
        else:
            print("Please select a reference image for Histogram Specification.")
    elif selected_operation == "Averaging filter":
        processed_image = apply_averaging_filter(imageInt)
    elif selected_operation == "Gaussian filter":
        processed_image = apply_Gaussian_filter(image)
    elif selected_operation == "Fourier transform":
        img_fourier = fourier_transform(image)
        img_reconstructed = fourier_inverse(img_fourier)
        processed_image = img_reconstructed
    elif selected_operation == "bilinear":
        try:
            new_width = int(new_width_entry.get())
            new_height = int(new_height_entry.get())
            processed_image = bilinear_interpolation(imageInt, new_width, new_height)
        except ValueError:
            print("Please enter valid numbers for new width and height.")
        if processed_image is not None:
            cv2.imshow("Processed Image", processed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    elif selected_operation == "nearest neighbor":
        try:
            new_width = int(new_width_entry.get())
            new_height = int(new_height_entry.get())
            processed_image = nn(imageInt, new_width, new_height)
        except ValueError:
            print("Please enter valid numbers for new width and height.")
        if processed_image is not None:
            cv2.imshow("Processed Image", processed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    elif selected_operation=="Huffman coding":
        _, _, huffman_codes = compress_image_with_huffman(imageInt)
        huffman_codes_str = '\n'.join([f'{k}: {v}' for k, v in huffman_codes.items()])
        messagebox.showinfo("Huffman Codes", huffman_codes_str)

  

window = tk.Tk()
window.title("Image Viewer")
window.geometry("1000x600")

adaptive_option_var = tk.StringVar()

button = tk.Button(window, text="Open Image", command=open_image)
button.place(x=50, y=50)

ref_button = tk.Button(window, text="Open Reference Image", command=open_reference_image)
ref_button.pack_forget()

label = tk.Label(window)
label.place(x=50, y=100)

ref_label = tk.Label(window)
ref_label.place(x=460, y=100)

options = [ "Median filter", "Adaptive filter", "Averaging filter", "Gaussian filter", 
            "Laplacian Operator", "Unsharp Masking and Highboost Filtering", 
           "Roberts Cross-Gradient Operators", "Sobel Operators",  "Impulse noise", 
           "Gaussian noise", "Uniform noise", "Histogram Equalization", 
           "Histogram Specification", "Fourier transform", "nearest neighbor","bilinear", "Huffman coding"]
selected_option = tk.StringVar(window)
selected_option.set("None")
dropdown = ttk.Combobox(window, textvariable=selected_option, values=options, state="readonly", width=30)
dropdown.place(x=400, y=50)
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

filter_frame = tk.Frame(window)
filter_frame.place(x=700, y=150)

buttonRun = tk.Button(window, text="Run", command=run_operation)
buttonRun.place(x=400, y=550)

window.mainloop()
