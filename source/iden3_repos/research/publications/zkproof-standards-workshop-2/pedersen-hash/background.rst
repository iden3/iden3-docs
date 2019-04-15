The Pedersen hash has already been defined and used by the ZCash team in
Sapling, their latest network upgrade :raw-latex:`\cite{sapling}`. They
construct it on the Jubjub elliptic curve and using 3-bit lookup tables.
In this document, we propose a different implementation of the Pedersen
hash function using Baby-Jubjub elliptic curve and 4-bit windows, which
requires less constraints per bit than using 3-bit windows.
