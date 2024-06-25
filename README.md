# region-splitting-and-merging
Image Processing Project: Grayscale Conversion and Image Splitting

Overview
This project focuses on image processing techniques using Python. The main tasks include converting an image to grayscale and splitting the grayscale image into smaller parts based on a given threshold. The splitting process is recursive and continues until the difference between the maximum and minimum pixel values in each part is less than the specified threshold.

Project Structure
convert_to_gray(image_path): Function to convert an image to grayscale.
split_image(image, threshold): Function to recursively split a grayscale image based on a pixel value threshold.
main.py: The main script that uses the above functions to process an image.

Dependencies
Pillow: Python Imaging Library (PIL) fork for opening, manipulating, and saving image files.
numpy: Library for numerical operations.

Acknowledgements
The project utilizes the Pillow library for image processing.
Numpy is used for efficient numerical operations.

Conclusion
This project demonstrates basic image processing techniques in Python, including grayscale conversion and recursive image splitting based on pixel intensity differences. It can be further extended to include more advanced image processing and analysis features.
