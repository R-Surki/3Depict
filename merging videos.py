#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:42:41 2024

@author: Roohallah Surki Aliabad roohallah.surkialiabad@oulu.fi
"""
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"

from moviepy.editor import VideoFileClip, clips_array

# Your video processing code here


# List of video file paths
video_files = ['10.mp4', '16.mp4', '35.mp4']

# Load video clips
clips = [VideoFileClip(video) for video in video_files]

# Resize videos to the same height (optional, if they have different sizes)
# Comment this line if all videos are already of the same height
clips = [clip.resize(height=360) for clip in clips]

# Combine videos side by side
final_clip = clips_array([clips])

# Output the final combined video
final_clip.write_videofile("output_combined.mp4", codec="libx264")
