from PIL import Image
import numpy as np
import cv2
import os

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('output.mp4', fourcc, 30, (320, 240))

files = os.listdir('./data')
for i in range(len(files)):
    path = os.path.join('./data', files[i])
    with open('./data/' + f'{i}'.zfill(4) + '.txt', 'r') as f:
        noise = f.readlines()

    noise = [list(map(int, x.strip())) for x in noise]
    array = np.array(noise).astype(np.uint8) * 255
    frame = cv2.cvtColor(array, cv2.COLOR_GRAY2BGR)
    video_writer.write(frame)

video_writer.release()
