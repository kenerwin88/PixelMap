FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install nodejs npm git iputils-ping wget -y
RUN npm install node-rsa web3 solc http-server -g
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN wget https://github.com/ethcore/parity/releases/download/v1.3.9/parity_1.3.9-0_amd64.deb
RUN dpkg -i parity_1.3.9-0_amd64.deb
COPY chain.json /home/chain.json
# pip install json-rpc web3
# pip install eth-testrpc
