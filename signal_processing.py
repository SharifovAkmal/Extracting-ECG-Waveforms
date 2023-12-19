import matplotlib.pyplot as plt
import numpy as np
import cv2

def apply_threshold(img, threshold_value):
    _, thresholded_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    inverted_img = cv2.bitwise_not(thresholded_img)
    return inverted_img

def create_color_mask(img, lower_color, upper_color):
    mask = cv2.inRange(img, lower_color, upper_color)
    return mask

def bitwise_and(img1, img2, mask):
    return cv2.bitwise_and(img1, img2, mask=mask)

def process_signal(img_gray):
    img_inverted = apply_threshold(img_gray, 115)

    lower_color = (0, 0, 0)
    upper_color = (110, 110, 110)
    color_mask = create_color_mask(img_gray, lower_color, upper_color)

    img_bitwise = bitwise_and(img_inverted, img_inverted, color_mask)

    len_img_rgb = len(img_gray)

    # plt.show()

    # Raw data processing
    draw_ecg_signal = []

    plt.plot(draw_ecg_signal)
    plt.show()