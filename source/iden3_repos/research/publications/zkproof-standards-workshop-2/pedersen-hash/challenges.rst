One of the main challenges to create this standard and to see it adopted
by the community is to provide correct, usable, and well-maintained
implementations in as many languages as possible.

Some effort is also required to audit and verify code coming from the
community and claiming to implement the 4-bit window Pedersen hash
function to prevent the propagation of potentially insecure
implementations.

Finally, the proposal as it stands today includes the padding of the
message :math:`M` to a multiple of four bits. There are potentials
issues with this approach where collisions can happen.
