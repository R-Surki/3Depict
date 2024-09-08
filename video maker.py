#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:19:25 2024

@author: Roohallah Surki Aliabad roohallah.surkialiabad@oulu.fi
"""

import cv2
import os

# Path to the folder containing PNG images
image_folder = 'img'
# Name of the output video file
video_name = 'img.mp4'
# Text to display
text = "Threshold= 16%"
# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)  # White color
thickness = 2
# Position of the text in the top-right corner with padding
padding = 10

# List all files in the folder and sort them (assuming filenames are ordered correctly)
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()

# Read the first image to get the width and height
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
video = cv2.VideoWriter(video_name, fourcc, 30.0, (width, height))

# Calculate the position for the text in the top-right corner
(text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
text_x = width - text_width - padding
text_y = text_height + padding

# Iterate over the images and write them to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    
    # Add text to the frame
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, thickness)
    
    # Write the frame to the video
    video.write(frame)

# Release the VideoWriter
video.release()

print("Video has been created successfully with text overlay.")
