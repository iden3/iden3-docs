| Consider the prime number

  .. math::

     p = 21888242871839275222246405745257275088548364
     400416034343698204186575808495617

   and let :math:`\Fp` be the finite field with :math:`p` elements. We
  define :math:`E_M` as the *Baby-Jubjub* Montgomery elliptic curve
  defined over :math:`\Fp` given by equation

  .. math:: E: v^2 = u^3 +  168698u^2 + u.

   The order of :math:`E_M` is :math:`n = 8\times l`, where

  .. math::

     l = 2736030358979909402780800718157159386076813972
     158567259200215660948447373041

   is a prime number. Denote by :math:`\G` the subgroup of points of
  order :math:`l`, that is,

  .. math:: \G = \Set{ P \in E(\Fp) | l P = O  }.

   Let

  .. math::

     \begin{aligned}
         B =  (17777552123799933955779906779655732241715742912184938656739573121738514868268,\\
     2626589144620713026669568689430873010625803728049924121243784502389097019475)\end{aligned}

   be a generator of :math:`\G`.
| :math:`E_M` is birationally equivalent to the Edwards elliptic curve

  .. math:: E: x^2 + y^2 = 1 +  d x^2 y^2

   where
  :math:` d = 9706598848417545097372247223557719406784115219466060233080913168975159366771.`
| The birational equivalence :raw-latex:`\cite[Thm. 3.2]{twisted}` from
  :math:`E` to :math:`E_M` is the map

  .. math:: (x,y) \to (u,v) = \left( \frac{1 + y}{1 - y} , \frac{1 + y}{(1 - y)x} \right)

   with inverse from :math:`E_M` to :math:`E`

  .. math:: (u, v) \to (x, y) = \left(  \frac{u}{v}, \frac{u - 1}{u + 1}   \right).
