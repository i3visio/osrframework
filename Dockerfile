FROM ubuntu:latest

MAINTAINER i3visio

# Updating packages
RUN apt-get update -y

# Installing Pip from repositories
RUN apt-get install -y python-pip

# Installing latest version of pip
RUN pip install pip --upgrade

# Installing latest version of pip
RUN pip install osrframework
