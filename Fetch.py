import praw

from gtts import gTTS

import cv2
import numpy as np
import os

language = "en"

# Authenticate with Reddit API (create an app on Reddit to get credentials)
reddit = praw.Reddit(client_id='--4aIpv-B1MVoeTfB0XGHg', #client ID
                     client_secret='rglR90rKQfksdsZwkCyPHciSioxz3g', #secret
                     user_agent='script by u/Worried-Wing9304')

# Choose a subreddit
subreddit = reddit.subreddit('PhotoshopRequest')

# Fetch hot posts (you can use other sorting methods like 'top', 'new', etc.)
for submission in subreddit.hot(limit=5):  # Fetching 5 hot posts
    print(submission.title)  # Print the title of each post
    print(submission.selftext)  # Print the text content of the post
    print('-------------------')
    
speech = gTTS(text = submission.title, lang = language, slow = False, tld = "us")
speech.save("test.mp3")


# Function to create a video from images with text overlays
def create_video(image_paths, texts, output_video_path, duration=5):
    frame_rate = 24  # Frames per second

    # Determine dimensions of the first image
    img = cv2.imread(image_paths[0])
    height, width, _ = img.shape

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4 format
    out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

    # Iterate through images and overlay text, then write to video
    for i, image_path in enumerate(image_paths):
        img = cv2.imread(image_path)

        # Add text overlay
        text = texts[i]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Repeat the frame for 'duration' seconds
        for _ in range(int(frame_rate * duration)):
            out.write(img)

    out.release()

# Example data (replace this with your logic to fetch images and text)
image_paths = ['reddit-how-to-post-4.jpg', 'reddit-how-to-post-4.jpg', 'reddit-how-to-post-4.jpg']
texts = ['Text 1', 'Text 2', 'Text 3']
output_video_path = 'output_video.mp4'

# Create the video
create_video(image_paths, texts, output_video_path, duration=5)

