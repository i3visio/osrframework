FROM ubuntu:latest

MAINTAINER i3visio

# Recover build-arg if requested
ARG VERSION

# Updating packages
RUN apt-get update -y

# Installing Pip from repositories
RUN apt-get install -y python-pip


# Install prelease version or stable version if requested
RUN pip install osrframework --upgrade $VERSION

# Patch to collect the configuration files
# ----------------------------------------
# For some reason, the Docker installation seems not to correctly set the default .cfg files.
RUN apt-get install -y wget

# We will download them manually for now.
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/accounts.cfg -O /root/.config/OSRFramework/default/accounts.cfg
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/api_keys.cfg -O /root/.config/OSRFramework/default/api_keys.cfg
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/browser.cfg -O /root/.config/OSRFramework/default/browser.cfg
RUN wget https://raw.githubusercontent.com/i3visio/osrframework/master/config/general.cfg -O /root/.config/OSRFramework/default/general.cfg
