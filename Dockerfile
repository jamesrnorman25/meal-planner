# FROM continuumio/miniconda3
# RUN conda config --add channels conda-forge
# RUN conda update --all

# COPY env.yml /opt/app/env.yml
# RUN conda env create --yes --file=/opt/app/env.yml

FROM python:3.7-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /opt/app/requirements.txt
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install -r /opt/app/requirements.txt

COPY src /src
WORKDIR /src

EXPOSE 8888


CMD gunicorn --bind :8888 dev_server.wsgi:application