FROM ubuntu:bionic

MAINTAINER paul.gullett@meetingroom.io

ARG OPENCV_VERSION=3.4.8
ARG VERSION=1.0
ARG DEBIAN_FRONTEND=noninteractive

ENV TZ=Europe/London

WORKDIR /root

RUN	apt update -qq && apt upgrade -y && \
		apt -y install \
		build-essential cmake \
		qt5-default libvtk6-dev \
		zlib1g-dev libjpeg-dev \
		libwebp-dev libpng-dev \
		libtiff5-dev \
		libopenexr-dev libgdal-dev \
		libdc1394-22-dev libavcodec-dev \
		libavformat-dev libswscale-dev \
		libtheora-dev libvorbis-dev \
		libxvidcore-dev libx264-dev \
		yasm libopencore-amrnb-dev \
		libopencore-amrwb-dev libv4l-dev \
		libxine2-dev libtbb-dev libeigen3-dev \
		python-dev python-tk pylint \
		python-numpy python3-dev python3-tk \
		pylint3 python3-numpy flake8 \
		ant default-jdk \
		doxygen unzip wget

RUN 	wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip && \
		unzip ${OPENCV_VERSION}.zip && rm ${OPENCV_VERSION}.zip && \
		mv opencv-${OPENCV_VERSION} OpenCV

RUN	cd OpenCV && mkdir build && cd build && \
		cmake -DWITH_QT=ON -DWITH_OPENGL=ON \
		-DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON \
		-DWITH_XINE=ON -DENABLE_PRECOMPILED_HEADERS=OFF .. && \
		make -j4 && \
		make install && \
		ldconfig
