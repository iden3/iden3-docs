| When using 3-bit and 4-bit windows, we have **1 constraint for the
  sign** and **3 for the sum** (as we are using the Montgomery form of
  the curve, that requires only 3). Now let’s look at the constraints
  required for the multiplexers.
| With 3-bit windows we need only one constraint per multiplexer, so **2
  constraints** in total.
| Standard 4-bit windows require two constraints: one for the output and
  another to compute :math:`s_0*s_1`. So, a priori we would need 4
  constraints, two per multiplexer. But we can reduce it to 3 as the
  computation of :math:`s_0*s_1` is the same in both multiplexers, so
  this constraint can be reused. This way only **3 constraints** are
  required.
| So, the amount of constraints per bit are:

-  3-lookup window : :math:` (1+3+2)/3 = 2 ` constraints per bit.

-  4-lookup window : :math:` (1 +3+3)/4 = 1.75 ` constraints per bit.

The specific constraints can be determined as follows: let the
multiplexers of coordinates :math:`x` and :math:`y` be represented by
the following look up tables:

+---------------+---------------+---------------+---------------+
| :math:`s_2`   | :math:`s_1`   | :math:`s_0`   | :math:`out`   |
+===============+===============+===============+===============+
| 0             | 0             | 0             | :math:`a_0`   |
+---------------+---------------+---------------+---------------+
| 0             | 0             | 1             | :math:`a_1`   |
+---------------+---------------+---------------+---------------+
| 0             | 1             | 0             | :math:`a_2`   |
+---------------+---------------+---------------+---------------+
| 0             | 1             | 1             | :math:`a_3`   |
+---------------+---------------+---------------+---------------+
| 1             | 0             | 0             | :math:`a_4`   |
+---------------+---------------+---------------+---------------+
| 1             | 0             | 1             | :math:`a_5`   |
+---------------+---------------+---------------+---------------+
| 1             | 1             | 0             | :math:`a_6`   |
+---------------+---------------+---------------+---------------+
| 1             | 1             | 1             | :math:`a_7`   |
+---------------+---------------+---------------+---------------+

+---------------+---------------+---------------+---------------+
| :math:`s_2`   | :math:`s_1`   | :math:`s_0`   | :math:`out`   |
+===============+===============+===============+===============+
| 0             | 0             | 0             | :math:`b_0`   |
+---------------+---------------+---------------+---------------+
| 0             | 0             | 1             | :math:`b_1`   |
+---------------+---------------+---------------+---------------+
| 0             | 1             | 0             | :math:`b_2`   |
+---------------+---------------+---------------+---------------+
| 0             | 1             | 1             | :math:`b_3`   |
+---------------+---------------+---------------+---------------+
| 1             | 0             | 0             | :math:`b_4`   |
+---------------+---------------+---------------+---------------+
| 1             | 0             | 1             | :math:`b_5`   |
+---------------+---------------+---------------+---------------+
| 1             | 1             | 0             | :math:`b_6`   |
+---------------+---------------+---------------+---------------+
| 1             | 1             | 1             | :math:`b_7`   |
+---------------+---------------+---------------+---------------+

We can express them with the following 3 constraints:

-  :math:`aux = s_0 s_1`

-  | :math:`out = [ (a_7-a_6-a_5+a_4-a_3+a_2+a_1-a_0)*aux 
                 + (a_6-a_4-a_2+a_0)*s_1`
   | :math:`\text{\qquad\;\;} + (a_5-a_4-a_1+a_0)*s_0
                 + (a_4 - a_0) ] z 
                 + (a_3-a_2-a_1+a_0)*aux + (a_2-a_0)*s_1 `
   | :math:`\text{\qquad\;\;} + (a_1-a_0)*s_0+ a_0`

-  | :math:` out = [ (b_7-b_6-b_5+b_4-b_3+b_2+b_1-b_0)*aux 
                 + (b_6-b_4-b_2+b_0)*s_1`
   | :math:`\text{\qquad\;\;} + (b_5-b_4-b_1+b_0)*s_0 
                 + (b_4 - b_0)] z 
                 + (b_3-b_2-b_1+b_0)*aux + (b_2-b_0)*s_1 \\
                 \text{\qquad\;\:} + (b_1-b_0)*s_0+ b_0`
