========
Tutorial
========

.. contents::    :depth: 3

circom and snarkjs tutorial
===========================

This tutorial will guide you in creating your first Zero Knowledge
zkSnark circuit. It will navegate across the various techniques to write
circuits and it will show you how to create proofs and verify them
off-chain and on-chain on Ethereum.

1. Installing the tools
-----------------------

1.1 Pre-requisites
~~~~~~~~~~~~~~~~~~

If you don’t have it installed yet, you need to install ``Node.js`` in
your laptop.

Last stable version of ``Node.js`` (Or 8.12.0) works just fine. But if
you install the latest current version ``Node.js`` (10.12.0) you will
see significant performance increase. This is because last versions of
node includes Big Integer Libraries nativelly. The ``snarkjs`` library
makes use of this feature if available, and this improves the
performance x10 (!).

1.2 Install **circom** and **snarkjs**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just run:

.. code:: sh

   npm install -g circom
   npm install -g snarkjs

2. Working with a circuit
-------------------------

Let’s create a circuit that tries to prove that you are able to factor a
number!

2.1 Create a circuit in a new directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create an empty directory called ``factor`` where you will put all
   the files that you will use in this tutorial.

::

   mkdir factor
   cd factor

..

   In a real circuit, you will probably want to create a ``git``
   repository with a ``circuits`` directory and a ``test`` directory
   with all your tests, and the needed scripts to build all the
   circuits.

2. Create a new file named ``circuit.circom`` with the following
   content:

::
   pragma circom 2.0.0;
   
   template Multiplier() {
       signal private input a;
       signal private input b;
       signal output c;
       
       c <== a*b;
   }

   component main = Multiplier();

This circuit has 2 private input signals named ``a`` and ``b`` and one
output named ``c``.

The only thing that the circuit does is forcing the signal ``c`` to be
the value of ``a*b``

After declaring the ``Multiplier`` template, we instantiate it with a
component named\ ``main``.

Note: When compiling a circuit a component named ``main`` must always
exist.

2.2 Compile the circuit
~~~~~~~~~~~~~~~~~~~~~~~

We are now ready to compile the circuit. Run the following command:

.. code:: sh

   circom circuit.circom -o circuit.json

to compile the circuit to a file named ``circuit.json``

3. Taking the compiled circuit to *snarkjs*
-------------------------------------------

Now that the circuit is compiled, we will continue with ``snarkjs``.
Please note that you can always access the help of ``snarkjs`` by
typing:

.. code:: sh

   snarkjs --help 

3.1 View information and stats regarding a circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To show general statistics of this circuit, you can run:

.. code:: sh

   snarkjs info -c circuit.json

You can also print the constraints of the circuit by running:

.. code:: sh

   snarkjs printconstraints -c circuit.json

3.2 Setting up using *snarkjs*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ok, let’s run a setup for our circuit:

.. code:: sh

   snarkjs setup 

..

   By default ``snarkjs`` will look for and use ``circuit.json``. You
   can always specify a different circuit file by adding
   ``-c <circuit JSON file name>``

The output of the setup will in the form of 2 files:
``proving_key.json`` and ``verification_key.json``

3.3. Calculating a witness
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before creating any proof, we need to calculate all the signals of the
circuit that match (all) the constrains of the circuit.

``snarkjs`` calculates these for you. You need to provide a file with
the inputs and it will execute the circuit and calculate all the
intermediate signals and the output. This set of signals is the
*witness*.

The zero knowledge proofs prove that you know a set of signals (witness)
that match all the constraints but without revealing any of the signals
except the public inputs plus the outputs.

For example, Imagine that you want to prove that you are able to factor
33 that means that you know two numbers ``a`` and ``b`` that when you
multiply them, it results in 33.

   Of course you can always use one and the same number as ``a`` and
   ``b``. We will deal with this problem later.

So you want to prove that you know 3 and 11.

Let’s create a file named ``input.json``

.. code:: json

   {"a": 3, "b": 11}

And now let’s calculate the witness:

.. code:: sh

   snarkjs calculatewitness

You may want to take a look at ``witness.json`` file with all the
signals.

Create the proof
~~~~~~~~~~~~~~~~

Now that we have the witness generated, we can create the proof.

.. code:: sh

   snarkjs proof

This command will use the ``prooving_key.json`` and the ``witness.json``
files by default to generate ``proof.json`` and ``public.json``

The ``proof.json`` file will contain the actual proof. And the
``public.json`` file will contain just the values of the public inputs
and the outputs.

Verifying the proof
~~~~~~~~~~~~~~~~~~~

To verify the proof run:

.. code:: sh

   snarkjs verify

This command will use ``verification_key.json``, ``proof.json`` and
``public.json`` to verify that is valid.

Here we are veifying that we know a witness that the public inputs and
the outputs matches the ones in the ``public.json`` file.

If the proof is ok, you will see an ``OK`` in the screen or ``INVALID``
otherwise.

Generate the solidity verifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   snarkjs generateverifier

This command will take the ``verification_key.json`` and generate a
solidity code in ``verifier.sol`` file.

You can take the code in ``verifier.sol`` and cut and paste in remix.

This code contains two contracts: Pairings and Verifier. You just need
to deploy the ``Verifier`` contract.

   You may want to use a test net like Rinkeby, Kovan or Ropsten. You
   can also use the Javascript VM, but in some browsers, the
   verification takes long and it may hang the page.

Verifying the proof on-chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The verifier contract deployed in the last step has a ``view`` function
called ``verifyProof``.

This function will return true if the proof and the inputs are valid.

To facilitiate the call, you can use snarkjs to generate the parameters
of the call by typing:

.. code:: sh

   snarkjs generatecall

Just cut and paste the output to the parameters field of the
``verifyProof`` method in Remix.

If every thing works ok, this method should return true.

If you just change any bit in the parameters, you can check that the
result will be false.

Bonus track
-----------

We can fix the circuit to not accept one as any of the values by adding
some extra constraints.

Here the trick is that we use the property that 0 has no inverse. so
``(a-1)`` should not have an inverse.

that means that ``(a-1)*inv = 1`` will be inpossible to match if ``a``
is one.

We just calculate inv by ``1/(a-1)``

So let’s modify the circuit:

::

   template Multiplier() {
       signal private input a;
       signal private input b;
       signal output c;
       signal inva;
       signal invb;
       
       inva <-- 1/(a-1);
       (a-1)*inva === 1;
       
       invb <-- 1/(b-1);
       (b-1)*invb === 1;    
       
       c <== a*b;
   }

   component main = Multiplier();

A nice thing of circom language is that you can split a <== into two
independent acions: <– and ===

The <– and –> operators Just assign a value to a signal without creating
any constraints.

The === operator just adds a constraint without assigning any value to
any signal.

The circuit has also another problem and it’s that the operation works
in Zr, so we need to guarantee too that the multiplication does not
overflow. This can be done by binarizing the inputs and checking the
ranges, but we will reserve it for future tutorials.

Where to go from here.
----------------------

You may want to read the `README <https://github.com/iden3/circom>`__ to
learn more features about circom.

You can also check a a library with many basic circuits lib
binaritzations, comparators, eddsa, hashes, merkle trees etc
`here <https://github.com/iden3/circomlib>`__ (Work in progress).

Or a exponentiation in the Baby Jub curve
`here <https://github.com/iden3/circomlib>`__ (Work in progress).

Final note
==========

There is nothing worst for a dev than working with a buggy compiler.
This is a very early stage of the compiler, so there are many bugs and
lots of works needs to be done. Please have it present if you are doing
anything serious with it.

And please contact us for any isue you have. In general, a github issue
with a small piece of code with the bug is very worthy!.

Enjoy zero knowledge proving!
