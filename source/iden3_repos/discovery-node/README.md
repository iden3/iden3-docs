# discovery-node [![Go Report Card](https://goreportcard.com/badge/github.com/iden3/discovery-node)](https://goreportcard.com/report/github.com/iden3/discovery-node) [![GoDoc](https://godoc.org/github.com/iden3/discovery-node?status.svg)](https://godoc.org/github.com/iden3/discovery-node)
Draft implementation of `discovery-node` of the decentralized discovery protocol over Pss Swarm


## Overview

![network00](https://raw.githubusercontent.com/iden3/discovery-node/master/docs/network00.png "network00")

Types of node:
- `gateway` (`passive`): are the nodes that only perform petitions, acting as gateways to the discovery network. This node can be trustless, as all the data that gets from the network and that is returned to its petitions, have the proofs of validity (merkleproofs)
- `active`: are the nodes that are answering requests, each identity trusts its active discovery-node


#### Node Storage
The `discovery-node` data storage is a leveldb database. It's organized with prefixes, where each type of data is stored under a prefix.

Databases:
- `dbOwnIds`: holds the data about the identities that the `discovery-node` manages
- `dbAnswCache`: holds the data about the discovered identites. Each data packet of a discovered identity, has a `timestamp`, the data packets are valid under a time window where the `timestamp` allows to determine if it's already valed or is too old

#### Sample discovery flow
Roles:
- `user`: user identity, from a phone/laptop device
- `Requester`: `discovery-node` that wants to know about one identity
- `Id_Agent`: `discovery-node` that knows the info about the identity, and is listening in `Swarm Pss` in the topic `id_discovery`

Flow when a `discovery-node` receives an Id discover request:

![flow00](https://raw.githubusercontent.com/iden3/discovery-node/master/docs/flow00.png "flow00")

Discovery flow:
1. `discovery-node` receives an https petition from the `user` asking for an identity info, from now, this `discovery-node` will be the `Requester`
2. `Requester` checks if already knows a fresh copy of the data packet of the identity
	- in case that has the data, checks that the `timestamp` is not too old
	- if the data is fresh, returns it and finishes the process
	- if the identity data was not in its databases, ask to the network for it (following steps)
3. `Requester` creates `Query` packet asking for who is the relay of identity `john@domain.eth`
4. `Requester` sends the `Query` packet into the `Swarm Pss` network under the topic `id_discovery`
	- the `Requester` waits a configured amount of time, if the `Answer` don't comes inside that time window, returns an error msg through https to the `user`
5. the `Id_Agent` server of that identity will receive the `Query` packet and will see that is a user under its umbrella
6. `Id_Agent` server will answer the `Answer` packet (with the proofs of validity, signature, etc) to the `Requester`
7. `Requester` receives the `Answer` packet (verifies the signature), and now knows how to reach the Relay node of `john@domain.eth`, and can answer to the `user`

```
Requester                       Id_Agent
   +                            +
   |                            |
   * 1                          |
   * 2                          |
   * 3                          |
   |             4              |
   +--------------------------->+
   |                            * 5
   |             6              |
   +<---------------------------+
   * 7                          |
   |                            |
   +                            +

```


#### Data structures
Each data packet that is sent over the network, goes with a `ProofOfWork`, and a `Signature` of the emmiter.

```go
// Service holds the data about a node service (can be a Relay, a NameServer, a DiscoveryNode, etc)
type Service struct {
	IdAddr       common.Address
	KademliaAddr []byte // Kademlia address
	PssPubK      PubK   // Public Key of the pss node, to receive encrypted data packets
	Url          string
	Type         string // TODO define type specification (relay, nameserver, etc)
	Mode         string // Active or Passive(gateway) (this only affects to discovery-node's type)
	ProofService []byte // TODO ProofClaimService data type (to be defined)
}

// Query is the data packet that a node sends to discover data about one identity
type Query struct {
	Version          string         // version of the protocol
	MsgId            string         // random msg id, to identify and relate Query and Answer
	AboutId          common.Address // About Who is requesting data (about which identity address)
	RequesterId      common.Address
	RequesterKAddr   []byte // Kademlia address
	RequesterPssPubK PubK   // Public Key of the pss node requester, to receive encrypted data packets
	InfoFrom         []byte // TODO to be defined
	Timestamp        int64
	Nonce            uint64 // for the PoW
}

// Answer is the data packet that a node sends when answering to a Query data packet
type Answer struct {
	Version   string // version of the protocol
	MsgId     string // random msg id, to identify and relate Query and Answer
	AboutId   common.Address
	FromId    common.Address
	AgentId   Service
	Services  []Service
	Timestamp int64
	Signature []byte
}
```


### Run

#### Run one node
```
go run *.go --config config0.yaml start
```

#### Run 3 nodes and test endpoints
```
bash run-tmux-demo.sh
```

### Test
Unit tests:
```
go test ./...
```


