= [draw, minimum size=2em] = [pin edge=to-,thin,black]

(in) :math:`x`; (xor0) [right of=in, node distance=1cm] ; (e0) [right
of=xor0] :math:`x^7`; (xor1) [right of=e0] ; (e1) [right of=xor1]
:math:`x^7`; (xorr-1) [right of=e1, node distance=4cm] ; (er-1) [right
of=xorr-1] :math:`x^7`; (xor) [right of=er-1] ; (out) [right of=xor,
node distance=1cm] :math:`y`;

(in) edge node (xor0); (xor0) edge node (e0); (e0) edge node (xor1);
(xor1) edge node (e1); (e1) edge[dotted] node (xorr-1); (xorr-1) edge
node (er-1); (er-1) edge node (xor); (xor) edge node (out);

| Our elements are of : Let :math:`\Fr` be the finite field with
  :math:`r` elements (determinat per ... ).

  .. math:: r =  21888242871839275222246405745257275088548364400416034343698204186575808495617

   The hash function used in the Merkle tree is MiMC-7 described in
  https://eprint.iacr.org/2016/492.pdf.
| The idea of this function: Our block cipher is constructed by
  iterating a round function :math:`r` times where each round consists
  of a key addition with the key :math:`k` , the addition of a round
  constant :math:`c_i\in \Fr`, and the application of a non-linear
  function defined as :math:`F(x) :=x^7` for :math:`x\in \Fr`. The
  ciphertext is finally produced by adding the key :math:`k` again to
  the output of the last round. Hence, the round function is described
  as :math:`F_i(x) = F(x) \xor k \xor c_i` where :math:`c_0 = c_r = 0`
  and the encryption process is defined as

  .. math:: E_k(x) = (F_{r-1} \circ F_{r-2} \circ ... \circ F_0)(x) \xor k.

Note that the random constants :math:`c_i` do not need to be generated
for every evaluation of MiMC-7. Instead the constants are fixed once and
can be hard-coded into the implementation on either side.

| The original paper describes the hash function using exponent 3. The
  choice of exponent 7 comes from the fact that 3 and :math:`r` are not
  coprime, and the optimal (in which sense?) choice of another exponent,
  according (following indications of) to page 20 of the document, is
  :math:`7`.
| The number of rounds is:

  .. math:: \text{nRounds} = \ceil*{\frac{\llog r}{\llog 7}} = 91
| The hash returns 140 bits, this is why Merkle trees are bounded by 140
  levels (it is the length of the whole path of a claim).
| Encadenar valors (tipu pel hash de H(v1, v2, v3, v4) etc.
