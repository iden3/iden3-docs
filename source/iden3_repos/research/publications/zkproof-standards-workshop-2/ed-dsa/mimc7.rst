| The hash function used in EdDSA is MiMC-7 based in paper
  :raw-latex:`\cite{mimc}`, which describes the hash using exponent 3.
  In this specification, we use exponent 7 (hence the name MiMC-7) as 3
  and :math:`l-1` are not coprime and 7 is the optimal choice for
  exponentiation :raw-latex:`\cite[Sec. 6]{mimc}`.
| Let :math:`\Fl` be the finite field with :math:`l` elements. The block
  cipher is constructed by iterating a round function :math:`r` times
  where each round consists of a key addition with the key :math:`k`,
  the addition of a round constant :math:`c_i\in \Fr`, and the
  application of a non-linear function defined as :math:`F(x) :=x^7` for
  :math:`x\in \Fl`. The ciphertext is finally produced by adding the key
  :math:`k` again to the output of the last round. Hence, the round
  function is described as :math:`F_i(x) = F(x) \xor k \xor c_i` where
  :math:`c_0 = c_r = 0` and the encryption process is defined as

  .. math:: E_k(x) = (F_{r-1} \circ F_{r-2} \circ ... \circ F_0)(x) \xor k.

As the random constants :math:`c_i` do not need to be generated for
every evaluation of MiMC-7, they are hard-coded into the implementation.
The generation of these constants and the required number of rounds is
described in section [sec-mimc].
