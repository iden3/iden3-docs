Let :math:`P\not= O` be a point of the twisted Edwards curve :math:`E`
of order strictly greater than 8 and let :math:`k` a binary number
representing an element of :math:`\Fp`. We describe the circuit used to
compute the point :math:`k\cdot P`.

#. First, we divide :math:`k` into chunks of 248 bits. If :math:`k` is
   not a multiple of 248, we take :math:`j` segments of 248 bits and
   leave a last chunk with the remaining bits. More precisly, write

   .. math::

      \begin{gathered}
              k = k_0 k_1 \dots k_j   \quad\text{with}\quad 
                  \begin{cases}
                  k_i = b^i_0 b^i_1 \dots b^i_{247}   \;\text{ for }  i = 0, \dots, j-1, \\
                  k_j = b^j_0 b^j_1 \dots b^j_s   \;\text{ with } s\leq 247.
                  \end{cases}
              \end{gathered}

    Then,

   .. math::

      \label{kP}
                  k\cdot P = k_0\cdot P + k_1\cdot 2^{248}P +\dots+ k_j\cdot 2^{248j}P.

    This sum is done using the following circuit. The terms of the sum
   are calculated separately inside the seq boxes and then added
   together.

   |image|

#. Each seq box takes a point of :math:`E` of the from
   :math:`P_i = 2^{248 i} P` for :math:`i=0,\dots,j-1` and outputs two
   points

   .. math::

      2^{248} \cdot P_i 
                  \quad \text{and} \quad
                  \sum_{n = 0}^{247} b_n \cdot 2^{n} \cdot P_i.

    The first point is the input of the next :math:`(i+1)`-th seq box
   (note that :math:` 2^{248} \cdot P_i = P_{i+1}`) whereas the second
   output is the computation of the :math:`i`-th term in expression
   ([kP]). The precise circuit is depicted in next two figures seq and
   window.

   | |image|

   |image|

   The idea of the circuit is to first compute some point

   .. math::

      Q = P_i + b_1 \cdot (2P_i) + b_2 \cdot (4P_i) 
                      + b_3 \cdot (8P_i) + \dots + b_{247} \cdot (2^{247}P_i),

    and output the point

   .. math:: Q - b_0 \cdot P_i.

    This permits the computation of :math:`Q` using the Montgomery form
   of Baby-Jubjub and only use twisted Edwards for the second
   calculation. The reason to change forms is that, in the calculation
   of the output, we may get a sum with input the point at infinity if
   :math:`b_0 = 0`.

   Still, we have to ensure that none of the points being doubled or
   added when working in :math:`E_M` is the point at infinity and that
   we never add the same two points.

   -  By assumption, :math:`P\not= O` and ord\ :math:`(P)>8`. Hence, by
      Lagrange theorem :raw-latex:`\cite[Corollary 4.12]{lagrange}`,
      :math:`P` must have order :math:`r`, :math:`2r`, :math:`4r` or
      :math:`8r`. For this reason, none of the points in :math:`E_M`
      being doubled or added in the circuit is the point at infinity,
      because for any integer :math:`m`, :math:`2^m` is never a multiple
      of :math:`r`, even when :math:`2^m` is larger than :math:`r`, as
      :math:`r` is a prime number. Hence, :math:`2^m \cdot P \not= O`
      for any :math:`m\in\Z`.

   -  Looking closely at the two inputs of the sum, it is easy to
      realize that they have different parity, one is an even multiple
      of :math:`P_i` and the other an odd multiple of :math:`P_i`, so
      they must be different points. Hence, the sum in :math:`E_M` is
      done correctly.

#. The last term of expression ([kP]) is computed in a very similar
   manner. The difference is that the number of bits composing
   :math:`k_j` may be shorter and that there is no need to compute
   :math:`P_{j+1}`, as there is no other seq box after this one. So,
   there is only output, the point
   :math:`k_j \cdot P_j = k_j\cdot 2^{248j} P`. This circuit is named
   seq’.

   |image|

.. |image| image:: Diag/Mult_by_scalar.png
.. |image| image:: Diag/Mult_by_scalar_SEQ.png
.. |image| image:: Diag/Mult_by_scalar_SEQ_window.png
.. |image| image:: Diag/Mult_by_scalar_SEQ_prime.png

