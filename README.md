This project processes .jpg or .png images by creating binary mask images where all color channels exceed a threshold (200 for 8-bit images). Masks are saved as lossless .png files, and the total count of "max" (white) pixels across all masks is logged.

**Requirements**

Python 3.x
Libraries: opencv-python, numpy
Install dependencies:

pip install opencv-python numpy

**Usage**
1. Place input images in the images/ folder.
2. Run the script.
  python mask_processor.py
3.Mask images are saved to output_images2/ and total masked pixel count is logged.

**Code Summary**

*Thresholding: Pixels are set to white if all channels > 200.
*Parallel Processing: Uses multiprocessing.Pool to speed up processing across CPU cores.
*Logging: Logs the total "max" pixel count.

**Sample log output:**

INFO - Total masked pixels across all images: 123456
