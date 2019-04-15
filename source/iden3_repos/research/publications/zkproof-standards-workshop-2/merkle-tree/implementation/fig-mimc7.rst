= [draw, minimum size=2em] = [pin edge=to-,thin,black]

(in) :math:`x`; (xor0) [right of=in, node distance=1cm] ; (e0) [right
of=xor0] :math:`x^7`; (xor1) [right of=e0] ; (e1) [right of=xor1]
:math:`x^7`; (xorr-1) [right of=e1, node distance=4cm] ; (er-1) [right
of=xorr-1] :math:`x^7`; (xor) [right of=er-1] ; (out) [right of=xor,
node distance=1cm] :math:`y`;

(in) edge node (xor0); (xor0) edge node (e0); (e0) edge node (xor1);
(xor1) edge node (e1); (e1) edge[dotted] node (xorr-1); (xorr-1) edge
node (er-1); (er-1) edge node (xor); (xor) edge node (out);
