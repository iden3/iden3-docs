The computation of the Pedersen hash has two steps: first, the
generation of the base points :math:`P_0, P_1, \dots, P_5` (we take
:math:`k=5`). This only needs to be done only once, as they can be
reused to compute hashes of other data [REF?]. Secondly, the calculation
of expression ([eq-ped]). We describe in terms of circuits how to do
such computation and provide an example explaining both steps.
