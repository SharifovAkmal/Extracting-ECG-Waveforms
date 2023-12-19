# Extracting Waveforms from ECG Images

## Overview

This project focuses on extracting II waveforms from ECG images using Python, OpenCV, and other libraries. The main goal is to process the full ECG data and extract only the II waveforms for further analysis. The project also provides raw data of the final results.

The II lead is a crucial component in ECG analysis, capturing information that is valuable for diagnosing various cardiac conditions. Its specific positioning on the body allows it to provide essential insights into the electrical activity of the heart, making II waveforms particularly useful for a comprehensive understanding of the ECG signal.

## Project Structure

- `main.py`: Main script orchestrating the process.
- `image_processing.py`: Functions for loading and processing images.
- `signal_processing.py`: Functions for processing the ECG signal.

## Usage

1. Install dependencies: `pip install matplotlib numpy opencv-python`
2. Run `main.py` to process the ECG signal.

## Dependencies

- `matplotlib` (version 3.7.1)
- `numpy` (version 1.23.5)
- `opencv-python` (version 4.7.0.72)

## Project Goal

The main goal of this project is to extract II waveforms from full ECG data for further analysis. II waveforms are particularly useful in ECG analysis due to their ability to capture specific information crucial for diagnosing cardiac conditions.

## Output Images

- Original Image: Result Images/Original_Image.png
- Extracted II Waveforms: Result Images/Extracting_Gray_Image.png

## References

No external sources or projects used.

## Contributors

- Sharifov Akmalbek Uktam Ugli

## License

This project is licensed under the [MIT License](LICENSE).