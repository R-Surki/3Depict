# 3Depict
Here you can find codes make using 3Depict PNG to Video Converter

This script converts a sequence of PNG images into a video file, with customizable text overlays on each frame. The script uses OpenCV for image processing and video creation.

Features

	•	Converts a folder of PNG images into a single MP4 video.
	•	Adds a specified text overlay to each image frame.
	•	Allows customization of the text’s font, size, color, position, and more.

Requirements

	•	Python 3.x
	•	OpenCV (cv2) library

You can install OpenCV using pip:

pip install opencv-python

Usage

	1.	Place your PNG images in a folder (e.g., 16/).
	2.	Modify the script parameters:
	•	image_folder: Path to your image folder.
	•	video_name: Name of the output video file.
	•	text: The text you want to overlay on the video.
	•	Adjust font settings as needed (font, font_scale, font_color, thickness, etc.).
	3.	Run the script:

python create_video.py

Output

The script generates an MP4 video with the specified name, containing all images from the folder, each with the text overlay.

License and Attribution

This code is provided under a permissive license that allows you to use, modify, and distribute it freely for any purpose. However, if you use this code in your own projects, publications, or presentations, you must include the following acknowledgment:

“This work makes use of code developed by Roohallah Surki Aliabad.”

