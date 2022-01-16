FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# user
RUN useradd -g users api && \
	rm -rf ~api && \
    cp -a ~root ~api && \
    mkdir ~api/work && \
    chown -R api:users ~api && \
    echo "root:docker\$7" | chpasswd


USER api

ENV USER=api \
    HOME=/home/api

WORKDIR $HOME/app
