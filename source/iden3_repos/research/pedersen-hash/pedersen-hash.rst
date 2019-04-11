*Baby-Jubjub* is birationally equivalent to the Montgomery elliptic
curve defined by

.. math:: E_M : v^2 = u^3 + 168698 u^2 + u.

 The birational equivalence from :math:`E` to :math:`E_M` is the map

.. math:: (x,y) \to (u,v) = \left( \frac{1 + y}{1 - y} , \frac{1 + y}{(1 - y)x} \right)

 with inverse from :math:`E_M` to :math:`E`

.. math:: (u, v) \to (x, y) = \left(  \frac{u}{v}, \frac{u - 1}{u + 1}   \right).

 These results are from :raw-latex:`\cite[Theorem 3.2]{twisted}`. When
adding points of elliptic curves in Montgomery form, one has to be
careful if the points being added are equal (doubling) or not (adding)
and if one of the points is the point at infinity
:raw-latex:`\cite{montgomery}`. Twisted Edwards curves have the
advantage that there is no such case distinction and doubling can be
performed with exactly the same formula as addition
:raw-latex:`\cite{twisted}`. In comparison, operating in Montgomery
curves is cheaper. In this section, we summarize how addition and
doubling is performed in both forms. For the exact number of operations
required in different forms of elliptic curves, see
:raw-latex:`\cite{operations-cost}`.

-  : Let :math:`\point{1}` and :math:`\point{2}` be points of the
   Baby-Jubjub twisted Edwards elliptic curve :math:`E`. The sum
   :math:`P_1 + P_2` is a third point :math:`P_3 = (x_3, y_3)` with

   .. math::

      \begin{aligned}
                  &\lambda = 168696 x_1x_2y_1y_2,\\
                  &x_3 = (x_1y_2 + y_1x_2) / (1 + \lambda),\\
                  &y_3 = (y_1y_2 - 168700 x_1x_2) / (1 - \lambda).
              \end{aligned}

    Note that the neutral element is the point :math:`O = (0,1)` and the
   inverse of a point :math:`(x,y)` is :math:`(-x,y)`.

-  : Let :math:`\point{1}\not=O` and :math:`\point{2}\not=O` be two
   points of the Baby-JubJub elliptic curve :math:`E_M` in Montgomery
   form.

   If :math:`P_1\not=P_2`, then the sum :math:`P_1 + P_2` is a third
   point :math:`P_3 = (x_3, y_3)` with coordinates

   .. math::

      \begin{aligned}
              \label{eq-ted}
              \begin{split}
                  &\Lambda = (y_2-y_1)/ (x_2-x_1),\\
                  &x_3 = \Lambda^2 - 168698 - x_1 - x_2,\\
                  &y_3 = \Lambda(x_1- x_3) - y_1.
              \end{split}
              \end{aligned}

    If :math:`P_1 = P_2`, then :math:`2\cdot P_1` is a point
   :math:`P_3 = (x_3, y_3)` with coordinates

   .. math::

      \begin{aligned}
              \label{eq-mont}
              \begin{split}
                  &\Lambda = (3x_1^2 + 2Ax_1 + 1)/ (2By_1),\\
                  &x_3 = B\Lambda^2 - A - 2x_1,\\
                  &y_3 = \Lambda(x_1- x_3) - y_1.
              \end{split} 
              \end{aligned}

1.2

Elliptic curve: Baby-Jubjub
===========================

Twisted Edwards form
--------------------

Montgomery form
---------------

Arithmetic on the elliptic curve
================================

Addition of points
------------------

Multiplication by a scalar
--------------------------

Pedersen hash
=============

[sec-ped]

Set of generators
-----------------

Computation
-----------

There is no overflow
--------------------

Number of constraints per bit
-----------------------------
