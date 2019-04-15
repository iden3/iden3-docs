1.2

Scope
=====

Motivation
==========

Background
==========

Terminology And Description
===========================

Generation Of Baby Jubjub
-------------------------

| In 2016, a group of researchers of IRPF designed a deterministic
  algorithm that, given a prime number :math:`p`, it returns the
  elliptic curve defined over :math:`\Fp` with smallest coefficient
  :math:`A` such that :math:`A-2` is a multiple of 4 and equation
  :math:`y^2 = x^3 + Ax^2 + x` describes a Montgomery curve. The
  assumption :math:`A-2` divisible by 4 comes from the fact that as this
  value is used in many operations, so trying to keep it smaller and
  divisible by four is a reasonable assumption
  :raw-latex:`\cite{generation-baby}`.
| SafeCurves is a project that checks some of the most common and known
  attacks on several elliptic curves. It also provides the algorithm it
  was used :raw-latex:`\cite{safe-curves}`.
| We considered the large prime number dividing the order of BN128 and
  run algorithm A.1 from :raw-latex:`\cite{generation-baby}`. The first
  elliptic curve it was returned satisfying SafeCurves criteria was the
  Montgomery curve with coefficient :math:`A = 168698`. We named this
  curve Baby Jubjub elliptic curve.

Definition Of Baby Jubjub
-------------------------

From now on, let

.. math::

   p = 21888242871839275222246405745257275088548364
                   400416034343698204186575808495617

 and :math:`\Fp` the finite field with :math:`p` elements.

Montgomery Form
~~~~~~~~~~~~~~~

We define :math:`E_M` as the *Baby-Jubjub* Montgomery elliptic curve
defined over :math:`\Fp` given by equation

.. math:: E: v^2 = u^3 +  168698u^2 + u.

 The order of :math:`E_M` is :math:`n = 8\times r`, where

.. math::

   r = 2736030358979909402780800718157159386076813972
           158567259200215660948447373041

 is a prime number. Denote by :math:`\G` the subgroup of points of order
:math:`r`, that is,

.. math:: \G = \Set{ P \in E(\Fp) | r P = O  }.

Edwards Form
~~~~~~~~~~~~

| :math:`E_M` is birationally equivalent to the Edwards elliptic curve

  .. math:: E: x^2 + y^2 = 1 +  d x^2 y^2

   where
  :math:` d = 9706598848417545097372247223557719406784115219466060233080913168975159366771.`
| The birational equivalence :raw-latex:`\cite[Thm. 3.2]{twisted}` from
  :math:`E` to :math:`E_M` is the map

  .. math:: (x,y) \to (u,v) = \left( \frac{1 + y}{1 - y} , \frac{1 + y}{(1 - y)x} \right)

   with inverse from :math:`E_M` to :math:`E`

  .. math:: (u, v) \to (x, y) = \left(  \frac{u}{v}, \frac{u - 1}{u + 1}   \right).

Arithmetic In Baby Jubjub
-------------------------

In this section we define how to operate in the elliptic curve group:
the addition of points and multiplication of a point by a scalar (an
element of :math:`\Fp`).

Addition Of Points
~~~~~~~~~~~~~~~~~~

Multiplication Of A Point Of :math:`E` By A Scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Challenges And Security
=======================

As required in the construction of Baby-Jubjub, the curve satisfies
SafeCurves criteria. This can be checked following
:raw-latex:`\cite{github-barry}`.

Implementation
==============

Barry WhiteHat:

-  https://github.com/barryWhiteHat/baby_jubjub

-  https://github.com/barryWhiteHat/baby_jubjub_ecc

Jordi Baylina:
https://github.com/iden3/circomlib/blob/master/src/babyjub.js

Intellectual Property
=====================
