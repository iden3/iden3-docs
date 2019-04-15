The 4-bit window Pedersen hash function is a secure hash function which
maps a sequence of bits to a compressed point on an elliptic curve
:raw-latex:`\cite{pedersen-gen}`.

This proposal aims to standardize this hash function for use primarily
within the arithmetic circuits of zero knowledge proofs, together with
other generic uses such as for Merkle tree or any use cases requiring a
secure hash function.

As part of the standard, the paper details the elliptic curve used for
the hash function, the process to compute the Pedersen hash from a given
sequence of bits, and the computation of the hash from a sequences of
bits using an arithmetic circuit—which can be used within zero knowledge
proofs.

Moreover the paper includes references to open-source implementations of
the Pedersen hash function which follows the computation process details
in this proposal.
