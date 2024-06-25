# from PIL import Image
# import numpy as np
# def convert_to_gray(image_path):
#     # Open the image
#     image = Image.open(image_path)
    
#     # Convert the image to RGB mode if it's not already in RGB
#     image = image.convert('RGB')
    
#     # Get image dimensions
#     width, height = image.size
    
#     # Create a new image in grayscale mode
#     gray_image = Image.new('L', (width, height))
    
#     # Iterate over each pixel in the image
#     for y in range(height):
#         for x in range(width):
#             # Get the pixel value at (x, y)
#             pixel = image.getpixel((x, y))
            
#             # Compute grayscale value using luminosity method
#             gray_value = int((pixel[0] + pixel[1] + pixel[2]) / 3)
            
#             # Update the pixel value in the grayscale image
#             gray_image.putpixel((x, y), gray_value)
    
#     return gray_image

# def split_image(in_image, threshold):
#     image = np.array(in_image)
#     rows, cols = image.shape
#     image_max = 0
#     image_min = float('inf')
    
#     # Find the maximum and minimum pixel values in the image
#     for i in range(cols):
#         for j in range(rows):
#             if image[j, i] > image_max:
#                 image_max = image[j, i]
#             if image[j, i] < image_min:
#                 image_min = image[j, i]
    
#     # Calculate the midpoint of rows and columns
#     mid_row, mid_col = rows // 2, cols // 2
    
#     # Split the image into four equal parts
#     top_left = Image.fromarray(image[:mid_row, :mid_col])
#     top_right = Image.fromarray(image[:mid_row, mid_col:])
#     bottom_left = Image.fromarray(image[mid_row:, :mid_col])
#     bottom_right = Image.fromarray(image[mid_row:, mid_col:])
    
#     return top_left, top_right, bottom_left, bottom_right                                          


# input_image_path = 'C:\\Users\\user\\Desktop\\cv_project\\data.jpg'

# gray_image = convert_to_gray(input_image_path)

# output_image_path = 'C:\\Users\\user\\Desktop\\cv_project\\converted.jpg'

# gray_image.save(output_image_path)

# print("Image converted to grayscale manually successfully.")

# print(type(gray_image))
# res1,res2,res3,res4=split_image(gray_image,200)

# out_path1='C:\\Users\\user\\Desktop\\cv_project\\converted1.jpg'
# out_path2='C:\\Users\\user\\Desktop\\cv_project\\converted12.jpg'
# out_path3='C:\\Users\\user\\Desktop\\cv_project\\converted3.jpg'
# out_path4='C:\\Users\\user\\Desktop\\cv_project\\converted4.jpg'
# res1.save(out_path1)
# res2.save(out_path2)
# res3.save(out_path3)
# res4.save(out_path4)
from PIL import Image
import numpy as np

def convert_to_gray(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to RGB mode if it's not already in RGB
    image = image.convert('RGB')
    
    # Get image dimensions
    width, height = image.size
    
    # Create a new image in grayscale mode
    gray_image = Image.new('L', (width, height))
    
    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the pixel value at (x, y)
            pixel = image.getpixel((x, y))
            
            # Compute grayscale value using luminosity method
            gray_value = int((pixel[0] + pixel[1] + pixel[2]) / 3)
            
            # Update the pixel value in the grayscale image
            gray_image.putpixel((x, y), gray_value)
    
    return gray_image

def split_image(image, threshold):
    image_array = np.array(image)
    rows, cols = image_array.shape
    
    # If the image size is zero, return an empty list
    if rows == 0 or cols == 0:
        return []
    
    # Find the maximum and minimum pixel values in the image
    image_max = np.max(image_array)
    image_min = np.min(image_array)
    
    # If the difference between maximum and minimum pixel values is less than the threshold, return the image as is
    if image_max - image_min <= threshold:
        return [image]
    
    # Calculate the midpoint of rows and columns
    mid_row, mid_col = rows // 2, cols // 2
    
    # Split the image into four equal parts
    top_left = Image.fromarray(image_array[:mid_row, :mid_col])
    top_right = Image.fromarray(image_array[:mid_row, mid_col:])
    bottom_left = Image.fromarray(image_array[mid_row:, :mid_col])
    bottom_right = Image.fromarray(image_array[mid_row:, mid_col:])
    
    # Recursively split each part
    split_images = []
    split_images.extend(split_image(top_left, threshold))
    split_images.extend(split_image(top_right, threshold))
    split_images.extend(split_image(bottom_left, threshold))
    split_images.extend(split_image(bottom_right, threshold))
    
    return split_images

# Input and output paths
input_image_path = 'C:\\Users\\user\\Desktop\\cv_project\\data.jpg'
output_folder_path = 'C:\\Users\\user\\Desktop\\cv_project\\'

# Convert the input image to grayscale
gray_image = convert_to_gray(input_image_path)

# Split the grayscale image based on threshold
threshold = 200
split_images = split_image(gray_image, threshold)

# Save the split images
for i, split_image in enumerate(split_images):
    out_path = f'{output_folder_path}split_image_{i + 1}.jpg'
    split_image.save(out_path)

print(f"{len(split_images)} images split successfully based on threshold {threshold}.")
