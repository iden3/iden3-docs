Let :math:`M` be a sequence of bits. The *Pedersen hash* function of
:math:`M` is defined as follows:

-  Let :math:`P_0,P_1,\dots,P_k` be uniformly sampled generators of
   :math:`\G` (for some specified integer :math:`k`).

-  Split :math:`M` into sequences of at most 200 bits and each of those
   into chunks of 4 bits [1]_. More precisely, write

   .. math::

      \begin{gathered}
              M = M_0M_1\dots M_l 
              \quad\text{where}\quad
              M_i = m_0m_1\dots m_{k_i}
              \quad\text{with}\quad 
              \begin{cases}
                  k_i = 49    \;\text{ for }  i = 0, \dots, l-1, \\
                  k_i \leq 49 \;\text{ for }  i = l,
              \end{cases}
          \end{gathered}

    where the :math:`m_j` terms are chunks of 4 bits
   :math:`[b_0\: b_1\: b_2\: b_3]`. Define

   .. math::

      enc(m_j) = (2b_3-1) 
              \cdot (1+b_{0}+2b_{1}+4b_{2})

    and let

   .. math:: \langle M_i \rangle = \sum_{j=0}^{k_i-1} enc(m_j) \cdot 2^{5j}.

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

.. [1]
   If :math:`M` is not a multiple of 4, pad :math:`M` to a multiple of 4
   bits by appending zero bits.
