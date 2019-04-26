========
Overview
========

.. contents::    :depth: 3

go-iden3
========

Go implementation of the iden3 system.

|Go Report Card| |Build Status|

Install
-------

::

    $ go get github.com/iden3/go-iden3

Usage
-----

-  Relay Documentation:
   https://github.com/iden3/go-iden3/blob/master/Relay.md
-  MerkleTree Documentation:
   https://github.com/iden3/go-iden3/blob/master/merkletreeDoc/merkletree.md
-  Backup Server Documentation:
   https://github.com/iden3/go-iden3/blob/master/cmd/backupserver/README.md

Documentation
-------------

Go Modules documentation: - |GoDoc| common - |GoDoc| core - |GoDoc| db -
|GoDoc| eth - |GoDoc| crypto - |GoDoc| merkletree - |GoDoc| utils -
|GoDoc| services/backupsrv - |GoDoc| services/centrauthsrv - |GoDoc|
services/claimsrv - |GoDoc| services/identitysrv - |GoDoc|
services/mongosrv - |GoDoc| services/namesrv - |GoDoc| services/rootsrv
- |GoDoc| services/signsrv

Testing
-------

``go test ./...``

WARNING
~~~~~~~

All code here is experimental and WIP

License
-------

go-iden3 is part of the iden3 project copyright 2018 0kims association
and published with GPL-3 license, please check the LICENSE file for more
details.

.. |Go Report Card| image:: https://goreportcard.com/badge/github.com/iden3/go-iden3
   :target: https://goreportcard.com/report/github.com/iden3/go-iden3
.. |Build Status| image:: https://travis-ci.org/iden3/go-iden3.svg?branch=master
   :target: https://travis-ci.org/iden3/go-iden3
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/common?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/common
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/core?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/core
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/db?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/db
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/eth?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/eth
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/crypto?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/crypto
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/merkletree?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/merkletree
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/utils?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/utils
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/backupsrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/backupsrv
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/centrauthsrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/centrauthsrv
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/claimsrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/claimsrv
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/identitysrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/identitysrv
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/mongosrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/mongosrv
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/namesrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/namesrv
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/rootsrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/rootsrv
.. |GoDoc| image:: https://godoc.org/github.com/iden3/go-iden3/services/signsrv?status.svg
   :target: https://godoc.org/github.com/iden3/go-iden3/services/signsrv
