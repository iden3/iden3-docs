| As we described in section [sec-computation], we use a windowed scalar
  multiplication algorithm with signed digits. Each 4-bit message chunk
  corresponds to a window called selector and each chunk is encoded as
  an integer from the set :math:`\{-8..8\}\backslash \{0\}`. This allows
  a more efficient lookup of the window entry for each chunk than if the
  set :math:`\{1..16\}` had been used, because a point can be
  conditionally negated using only a single constraint
  :raw-latex:`\cite{sapling}`.
| As there are up to 50 segments per each generator :math:`P_i`, the
  largest multiple of the generator :math:`P_i` is :math:`n\cdot P_i`
  with

  .. math:: n = 2^0 \times8 + 2^5 \times 8 + \left(2^5\right)^2 \times8 \dots +   2^{245}\times 8 .

   To avoid overflow, this number should be smaller than
  :math:`(r-1)/2`. Indeed,

  .. math::

     \begin{aligned}
         \quad\; n 
         & = 8 \times \sum_{ k = 0}^{49} 2^{5k}
         = 8 \times \frac{2^{250}-1}{2^5-1}\\
         & = 466903585634339497675689455680193176827701551071131306610716064548036813064%\\\end{aligned}

   and

  .. math::

     \begin{aligned}
         \frac{r-1}{2} &= 1368015179489954701390400359078579693038406986079283629600107830474223686520 \\
         & > n.\\ \vspace{0.4cm}\end{aligned}
