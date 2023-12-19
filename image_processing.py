import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_image(file_path):
    img = cv2.imread(file_path)
    return img

def display_image(img, title=''):
    plt.figure(figsize=(10, 10))
    plt.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
    plt.title(title)
    plt.show()

def process_image(img_src):
    img_rgb = cv2.cvtColor(img_src, cv2.COLOR_BGR2RGB)
    img_rgb_crop = img_rgb[930:len(img_rgb)-50][:]
    img_gray = cv2.cvtColor(img_rgb_crop, cv2.COLOR_RGB2GRAY)

    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)

    display_image(img_rgb, 'Original Image (RGB)')
    display_image(img_gray, 'Gray Image')

    return img_gray