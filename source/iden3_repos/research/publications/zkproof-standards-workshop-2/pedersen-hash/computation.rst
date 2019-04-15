In the following circuit pedersen hash, we have depicted the circuit
used to compute the Pedersen hash of a message :math:`M` described in
equation [eq-ped]. Each multiplication box returns a term of the sum.

|image| |image|

As the set of generators are fixed, we can precompute its multiples and
use 4-bit lookup windows to select the right points. This is done as
shown in the circuit called selector. This circuit receives 4-bit chunk
input and returns a point. The first three bits are used to select the
right multiple of the point and last bit decides the sign of the point.
The sign determines if the :math:`x`-coordinate should be taken positive
or negative, as with Edwards curves, negating a point corresponds to the
negation of its first coordinate.

|image|

.. |image| image:: figures/pedersen-hash.png
.. |image| image:: figures/pedersen-multiplication.png
.. |image| image:: figures/pedersen-multiplication-selector.png

