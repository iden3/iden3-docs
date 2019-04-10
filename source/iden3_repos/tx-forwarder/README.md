# tx-forwarder
Server that forwards the tx to the specified smart contract.


## Usage

### Config
Deploy contract:
```
./tx-forwarder deploy
```
This will print the deployed contract address, then copy&paste in the config file `config.yaml`:
```
server:
        serviceapi: 0.0.0.0:11000
        adminapi: 0.0.0.0:11001
web3:
        url: http://127.0.0.1:8545
keystore:
        path: /var/config/keystore
        address: 0x123456789...
        passwd: /var/config/keystore.password
        keyjsonpath: /var/config/keystore/UTC-etc
contracts:
        samplecontract: 0xasdf
```

### Run
Then, run the server:
```
./tx-forwarder start
```

### Contract
Current contract is just a working sample contract.

The contract handlers goes inside `eth/contract/` directory.

Once having the contract file written in Solidity, in order to generate the Go handlers:
```
solc --abi --bin SampleContract.sol -o build
abigen --bin=./build/SampleContract.bin --abi=./build/SampleContract.abi --pkg=SampleContract --out=SampleContract.go
```
And place the `sampleContract.go` file in the `eth/contract/sampleContract.go` path.
