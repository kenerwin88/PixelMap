# DevOps Library Ethereum Demo
FROM ubuntu:14.04
MAINTAINER DevOps Library <admin@devopslibrary.com>
EXPOSE 8545:8545
EXPOSE 30303:30303

# Environment Variables
ENV nodekey ''
ENV staticNodes ''
ENV mine ''

# Install Ethereum
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d
RUN sudo apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository -y ppa:ethereum/ethereum
RUN sudo apt-get update
RUN apt-get install ethereum -y
COPY genesis.json /
COPY password.txt /
COPY run.sh /
RUN chmod a+x /run.sh

# Entrypoint
ENTRYPOINT ["/run.sh"]
