FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# deps
RUN apt update -y
RUN apt install -y --no-install-recommends apt-utils
RUN apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa


RUN apt install -y gcc postgresql-client python3.10-dev libc-dev libpq-dev locales \
    python3.10 curl python3.10-distutils


# locale
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8


# user
RUN useradd -g users api && \
	rm -rf ~api && \
    cp -a ~root ~api && \
    mkdir ~api/work && \
    chown -R api:users ~api && \
    echo "root:docker\$7" | chpasswd
USER api


# env
ENV USER=api \
    HOME=/home/api
ENV USER_BIN_PATH=${HOME}/.local/bin
ENV PATH $PATH:${USER_BIN_PATH}

# python deps
RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
RUN python3.10 /tmp/get-pip.py
RUN python3.10 -m pip install --upgrade pip
RUN python3.10 -m pip install pipenv

COPY Pipfile* /tmp/
ENV PYTHONUNBUFFERED 1

RUN cd /tmp && pipenv lock -d --requirements > requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY . $HOME/app

# Clean
USER root
RUN rm -rf /root/.cache/pip && apt-get clean
