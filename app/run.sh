#!/bin/bash
set -e
geth init genesis.json
geth --password password.txt account new
echo $nodekey > /root/.ethereum/nodekey
echo $staticNodes > /root/.ethereum/static-nodes.json
geth $mine --networkid 15 --nodiscover --rpc --rpcaddr 0.0.0.0 -rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3"
exec "$@"
