FROM ffmpegopencv:latest as build
MAINTAINER paul.gullett@meetingroom.io

ARG VERSION=1.0

ARG DEBIAN_FRONTEND=noninteractive

ENV TZ=Europe/London

WORKDIR /root

RUN 	rm -rf OpenCV 			&& \
	apt remove -y			  \
	build-essential cmake 		  \
	qt5-default libx264-dev		  \
	ant default-jdk 		&& \
	apt clean			&& \
	rm -rf /var/lib/apt/lists/*	&& \
	apt autoremove -y

FROM scratch

COPY --from=build / /

WORKDIR /root

RUN 	apt update 			&& \
	apt upgrade -y			&& \
	apt install -y curl unzip libxcb1 \
		libxcb-shm0 libxcb-shape0 \
		libxcb-xfixes0 libasound2 \
		libsdl2-2.0-0 libxv1	  \
		libass9 libx264-152 	  \
		libx265-146 libvpx5 	  \
		libfdk-aac1 \
		libmp3lame0 libopus0	  \
		jq pwgen bc less cron

RUN 	cd /root			&& \
	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" \
	-o "awscliv2.zip"		&& \
	unzip awscliv2.zip		&& \
	aws/install			&& \
	rm -rf aws awscliv2.zip

COPY	bin bin
COPY	.aws .aws

RUN	mkdir processdir
CMD	["/root/bin/fileprocesstest"]
