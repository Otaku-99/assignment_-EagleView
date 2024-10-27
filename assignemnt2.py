import cv2
import os
import numpy as np
from multiprocessing import Pool, cpu_count
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directory paths
input_dir = "images"
output_dir = "output_images2"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Threshold for creating the mask
THRESHOLD = 200  # For max of 8-bit images

# Function to process each image
def processing_image(file_path):
    # Read the image
    image = cv2.imread(file_path)
    
    if image is None:
        logging.error(f"Failed to load image: {file_path}")
        return 0
    mask = cv2.inRange(image, (THRESHOLD, THRESHOLD, THRESHOLD), (255, 255, 255))

    # Save the mask image as a lossless PNG
    base_name = os.path.basename(file_path)
    output_path = os.path.join(output_dir, os.path.splitext(base_name)[0] + "_mask.png")
    cv2.imwrite(output_path, mask)

    # Count the number of white pixels (mask pixels)
    mask_pixel_count = np.count_nonzero(mask)
    return mask_pixel_count

# Function to collect images and process them in parallel
def main():
    # List all image files in the input directory
    image_files_folder = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.lower().endswith((".jpg", ".png"))]

    # Initialize a Pool of workers based on the number of CPU cores
    with Pool(cpu_count()) as pool:
        # Process images in parallel and retrieve masked pixel counts
        mask_pixel_counts = pool.map(processing_image, image_files_folder)

    # Sum the masked pixel counts across all images
    total_masked_pixels = sum(mask_pixel_counts)
    logging.info(f"Total masked pixels across all images: {total_masked_pixels}")

if __name__ == "__main__":
    main()
