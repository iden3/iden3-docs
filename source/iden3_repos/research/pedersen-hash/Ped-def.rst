Let :math:`M` be a sequence of bits. We construct the Pedersen hash of
:math:`M` as follows:

-  Sample :math:`P_0,P_1,\dots,P_k` uniformly in :math:`\G` (for some
   specified integer :math:`k`).

-  Split :math:`M` into sequences of 4 bits [1]_. More precisely, write

   .. math::

      \begin{gathered}
              M = M_1M_2\dots M_l 
              \quad\text{where}\quad
              M_i = m_1m_2\dots m_{k_i}
              \quad\text{with}\quad 
              \begin{cases}
                  k_i = 50    \;\text{ for }  i = 0, \dots, l-1, \\
                  k_l \leq 50,
              \end{cases}
          \end{gathered}

    where the :math:`m_j` terms are 4-bit chunks
   :math:`[b_0^j\: b_1^j\: b_2^j\: b_3^j]`. Define

   .. math::

      enc(m_j) = (2b_3^j-1) 
              \cdot (1+b_{0}^j+2b_{1}^j+4b^j_{2})

    and let

   .. math:: \langle M_i \rangle = \sum_{j=1}^{k_i} enc(m_j) \cdot 2^{5(j-1)}.

    We define the Pedersen hash of :math:`M` as

   .. math::

      \label{eq-ped}
              H(M) = \langle M_0 \rangle \cdot P_0 
              +  \langle M_1 \rangle \cdot P_1 
              +  \langle M_2 \rangle \cdot P_2 
              + \dots + \langle M_l \rangle \cdot P_l.

    Note that the expression above is a linear combination of elements
   of :math:`\G`, so itself is also an element of :math:`\G`. That is,
   the resulting Pedersen hash :math:`H(M)` is a point of the elliptic
   curve :math:`E` of order :math:`r`.

The computation of the Pedersen hash has two steps: first, the base
points :math:`P_0, P_1, \dots, P_k` need to be generated. This only
needs to be done once, as they can be reused to compute hashes of other
data. And secondly, the calculation of expression ([eq-ped]). The
circuits used to compute this sum are quite similar to the ones used to
calculate the multiple of a point of an elliptic curve except that here
we only work with the twisted Edwards form of :math:`E` and we can have
many points precalculated, so instead of doubling all the time, we work
with look-up tables.

.. [1]
   If :math:`M` is not a multiple of 4, pad :math:`M` to a multiple of 4
   bits by appending zero bits.
