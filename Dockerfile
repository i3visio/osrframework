FROM ubuntu:latest

MAINTAINER i3visio

# Updating packages
RUN apt-get update -y

# Installing Pip from repositories
RUN apt-get install -y python-pip

# Installing latest version of pip
RUN pip install pip --upgrade

# Installing latest version of pip
RUN pip install osrframework --pre

# TODO: For some reason, the Docker installation seems not to correctly set the default .cfg files.
RUN sudo apt-get install -y wget

# We will download them manually for now.
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/accounts.cfg -O /root/.config/OSRFramework/default/accounts.cfg
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/api_keys.cfg -O /root/.config/OSRFramework/default/api_keys.cfg
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/browser.cfg -O /root/.config/OSRFramework/default/browser.cfg
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/general.cfg -O /root/.config/OSRFramework/default/general.cfg
