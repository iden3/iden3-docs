.. _repositories:

Services and Infrastructure 
##############################################

Basic services and infrastructure libraries.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Repo
     - Description
   * - iden3js_
     - Javascript client library                    
   * - go-iden3_
     - Go implemenation of the iden3 system   
   * - tx-forwarder_
     - Implementation of server that pays gas on behalf of user signed transactions for specified 
       smart contracts in ethereum blockchain   
   * - discovery-node_
     - Decentralized discovery protocol implementation          
   * - notification-server_
     - Implementation of a notification server to  push notifications to user identity wallets 

.. _iden3js: https://github.com/iden3/iden3js  
.. _go-iden3: https://github.com/iden3/go-iden3  
.. _tx-forwarder: https://github.com/iden3/tx-forwarder 
.. _discovery-node: https://github.com/iden3/discovery-node 
.. _notification-server: https://github.com/iden3/notifications-server 

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Services & Infrastructure:

   iden3_repos/iden3js
   iden3_repos/go-iden3
   iden3_repos/tx-forwarder
   iden3_repos/discovery-node
   iden3_repos/notifications-server


Zero Knowledge Proof 
#####################
zkSNARKs related utilities.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Repo
     - Description
   * - circom_ 
     - zkSNARKs circut compiler
   * - circomlib_
     -  Circuit libraries implementedin in circom
   * - snarkjs_
     - zkSNARKs Javascript implementation (setup, proof, verifier and witness generation)
   * - wasmsnark_ 
     - A fast zkSNARKs proof generator written in native Web Assembly

.. _circom: https://github.com/iden3/circom
.. _circomlib: https://github.com/iden3/circomlib
.. _snarkjs: https://github.com/iden3/snarkjs
.. _wasmsnark: https://github.com/iden3/wasmsnark

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: ZKProof:

   iden3_repos/circom
   iden3_repos/circomlib
   iden3_repos/snarkjs
   iden3_repos/websnark

Misc
####
Miscellaneous utilities.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Repo
     - Description
   * - wasmbuilder_ 
     - Javascript library to simplify writing Web Assembly code


.. _wasmbuilder: https://github.com/iden3/wasmbuilder


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Misc:

   iden3_repos/wasmbuilder
