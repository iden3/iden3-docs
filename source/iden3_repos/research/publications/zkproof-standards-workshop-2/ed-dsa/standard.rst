1.2

Scope
=====

This proposal aims to standarize the elliptic curve signature scheme
Edwards-curve Digital Signature Algorithm (EdDSA) for Baby Jubjub
Edwards elliptic curve using MiMC-7 hash function.

Motivation
==========

EdDSA is a variant of Schnorr’s signature scheme and it provides high
performance on a variety of platforms :raw-latex:`\cite{eddsa}`.

Background
==========

| There are many implementations of EdDSA with Edwards elliptic curves
  such as Ed25519 or Ed448-Goldilocks and most of them use hash SHA-512.
  This is the first document specifying a protocol for implementing
  EdDSA using MiMC-7 and we describe it on the Baby Jubjub Elliptic
  curve.
| The choice of the MiMC-7 hash function makes computations inside
  circuits very efficient and it has a big potential in zero knowledge
  protocols such as zk-SNARK.

Terminology
===========

The table below summarizes the terminology used across the document.
Each element is explained in greater detail in the following sections.

+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| **Notation**                      | **Description**                                                                                       |
+===================================+=======================================================================================================+
| :math:`p`                         | Prime number.                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`\Fp`                       | Finite field with :math:`p` elements.                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`E`                         | Baby Jubjub elliptic curve (defined over :math:`Fp`) in Edwards form.                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`E_M`                       | Baby Jubjub elliptic curve (defined over :math:`Fp`) in Montgomery form.                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`l`                         | Large prime number dividing the order of Baby Jubjub.                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`\Fl`                       | Finite field with :math:`l` elements.                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`\G`                        | Group of :math:`\Fp`-rational points of order :math:`l`.                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`B`                         | Base point (generator of :math:`\G`) of Baby Jubjub.                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`A = (A_x, A_y)`            | Public key. :math:`A` is a point on :math:`E`.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`k`                         | Private key.                                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`M`                         | Message. :math:`M` is an element of :math:`\Fl`.                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`(R,S) = ((R_x, R_y), S)`   | Signature on :math:`M`. :math:`R` is a point on :math:`E` and :math:`S` and element of :math:`\Fl`.   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`H`                         | Hash function MiMC-7.                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`r`                         | Number of rounds of MiMC-7.                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| :math:`c_0, c_1, \dots, c_r`      | Constants used in MiMC-7.                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+

[tab:notation]

Baby-Jubjub
-----------

MiMC-7
------

EdDSA
-----

The description of this protocol is based in :raw-latex:`\cite{eddsa}`:
Let the public key be a point :math:`A = (A_x, A_y)\in E` of order
:math:`l` and :math:`M` a message we wish to sign. The signature on
:math:`M` by :math:`A` consists of a par :math:`(R,S)` where
:math:`R = (R_x, R_y)` is a point of order :math:`l` of :math:`E` and
:math:`S\in\Fl\backslash\{0\}` such that

.. math:: 8SB = 8R + 8H(R,A,M)A.

Challenges and security
=======================

One of the main challenges to create this standard and to see it adopted
by the community is to provide correct, usable, and well-maintained
implementations in as many languages as possible. Some effort is also
required to audit and verify code coming from the community and claiming
to implement EdDSA for Baby Jubjub to prevent the propagation of
potentially insecure implementations. Part of the work in progress of
looking batch verification of short signatures. Lastly, the proposal as
it stands uses MiMC-7 as hash function as it works very optimal inside
circuits. We believe some work is required to determinate the security
MiMC hash functions.

Implementation
==============

In this section, we specify how each of the main operations in the
following EdDSA circuit are computed:

|image|

Operations in the elliptic curve
--------------------------------

Addition of points
~~~~~~~~~~~~~~~~~~

Multiplication of a point of :math:`E` by a scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MiMC-7
------

The specifications we use in the hash are (*we are working in explaining
this section in greater detail*):

#. Number of rounds: :math:` r = \ceil*{\frac{\llog l}{\llog 7}} = 91. `

#. Inputs:

   -  Coordinates of the public key: (:math:`A_x, A_y`).

   -  Coordinates of the point :math:`8R`: (:math:`R8_x, R8_y`).

   -  Message :math:`M`.

#. Number of inputs: 5.

#. Generation of constants:
   https://github.com/iden3/circomlib/blob/master/src/mimc7.js.

Example and test vectors
------------------------

*Work in progress.*

Existing implementations
------------------------

| EdDSA for Baby Jubjub implemented by Jordi Baylina in circom (zero
  knowledge circuit compiler):
| https://github.com/iden3/circomlib/blob/master/circuits/eddsamimc.circom

Intellectual Property
=====================

We will release the final version of this proposal under creative
commons, to ensure it is freely available to everyone.

.. |image| image:: circuit-eddsa.png

