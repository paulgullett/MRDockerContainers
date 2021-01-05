# MRDockerContainers

Code to create the containers for the meetingRoom server applications.

###### ffmpegopencv

Builds the base image that includes OpenCV 3.4.8 which is required for the Facebook transform360 element in ffmpeg. Doesn't currently build ffmpeg, but this will be included.

###### videoprocess

Uses ffmpegopencv to create the image that is used by ECS to process video files for use within the app.
