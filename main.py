from image_processing import load_image, process_image
from signal_processing import process_signal

def main():
    img_src = load_image("Data/AT_variable.png")
    processed_img = process_image(img_src)
    process_signal(processed_img)

if __name__ == "__main__":
    main()