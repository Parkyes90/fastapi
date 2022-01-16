FROM python:3.10-alpine

ARG DEBIAN_FRONTEND=noninteractive


# env
ENV USER=api \
    HOME=/home/api
ENV USER_BIN_PATH=${HOME}/.local/bin
ENV PATH $PATH:${USER_BIN_PATH}

# group
RUN addgroup $USER

# user
RUN adduser \
    --disabled-password \
    --home "$HOME" \
	--ingroup "$USER" \
    "$USER"

USER api


## python deps
RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv

COPY Pipfile* /tmp/
ENV PYTHONUNBUFFERED 1

RUN cd /tmp && pipenv lock -d --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . $HOME/app

CMD ["uvicorn", "main:app", "--reload"]