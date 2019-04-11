.. raw:: latex

   \maketitle 

.. raw:: latex

   \vspace{1cm}

.. raw:: latex

   \tableofcontents

.. raw:: latex

   \vspace{0.5cm}

Scope
=====

A section specifying the scope of the standard, highlighting what is
being standardized and what is not.

Motivation
==========

A section describing at least one concrete application motivating the
proposed standard, including an explanation of why the community will
benefit from such a standard.

Background
==========

A section introducing the problem, including definitions, references to
previous work and other background details.

Terminology
===========

For consistency across documents, adopt throughout the proposal,
terminology and definitions used in the ZKProof proceedings, with
pointers to the relevant sections.

Challenges
==========

For motivating the discussions, highlight the main challenges in
creating such a standard, as well as any open or unresolved questions.

Security
========

If relevant, provide a proof of security in the description.

Implementation
==============

If relevant, submit an open source prototype implementation (by
including a reference to the repository with the code).

Intellectual Property
=====================

We aim to ensure that proposals can be freely implemented. Thus,
proposals should disclose the existence of any known patents (awarded or
pending) which may restrict free implementation. This may affect the
decision process, and a detailed policy is being developed.

Submission Requirements

Submissions must be prepared in LaTeX in 11-point font; there is no page
limit. We encourage submission of every proposal, even if not finalized,
because even discussing in-progress proposals is valuable to the
community. To submit your proposal send an email with the PDF document
at contact@zkproof.org with every author in CC.

Submissions must have the following structure:

-  Title: proposal title, author names, and affiliations.

-  Scope: a section specifying the scope of the standard, highlighting
   what is being standardized and what is not.

-  Motivation: a section describing at least one concrete application
   motivating the proposed standard, including an explanation of why the
   community will benefit from such a standard.

-  Background: a section introducing the problem, including definitions,
   references to previous work and other background details.

And should address the following points:

-  Terminology: for consistency across documents, adopt throughout the
   proposal, terminology and definitions used in the ZKProof
   proceedings, with pointers to the relevant sections.

-  Challenges: for motivating the discussions, highlight the main
   challenges in creating such a standard, as well as any open or
   unresolved questions.

-  Security: if relevant, provide a proof of security in the
   description.

-  Implementation: if relevant, submit an open source prototype
   implementation (by including a reference to the repository with the
   code).

-  Intellectual Property: we aim to ensure that proposals can be freely
   implemented. Thus, proposals should disclose the existence of any
   known patents (awarded or pending) which may restrict free
   implementation. This may affect the decision process, and a detailed
   policy is being developed.

Initial Timeline

Each community standard proposal will be reviewed by the Proposals
Committee (PC) and, if deemed appropriate, will be subsequently
discussed in the second workshop. After the workshop, a second draft
that includes the suggestions and comments from the discussions must be
submitted. Authors of accepted proposals must attend the workshop and
must submit each draft in a timely manner, according to the timeline
below. After the initial submission, failure to submit the further
drafts may result in a rejection of the proposal. Alternatively the
Steering Committee (SC) may assign others to continue leading the
proposal.

-  March 1st, 2019, 23:59 (UTC): submission of the first draft of
   proposals are due

-  March 20th, 2019: decisions by the PC are communicated to the authors

-  April 10th, 2019: community discussions start at the workshop,
   moderated by the PC

-  May 15th, 2019, 23:59 (UTC): submission of the second draft of
   proposals are due

Online Discussions

After the workshop, shepherds will be assigned to each working draft in
order to moderate online discussions that will take place in an open
forum (to be determined). The shepherds will attempt to reach consensus
by the community on different topics and will publish a “Last Call” and
due date for final comments and suggestions. Once these final changes
have been made, the shepherds will review the final drafts and submit
them to the SC for approval as a Community Standard. Topics

Proposals on any topic related to zero zero-knowledge proofs are
welcome, including:

-  Terminology

   -  Motivation: the first thing to be standardized should be
      terminology, language and definitions. The field of zero knowledge
      is packed with terms and concepts that require careful
      definitions, which vary across the literature (see Security and
      Implementation tracks).

   -  Proposal example: provide a unified glossary encompassing all
      (implicit and explicit) terminology in the proceeding documents.

-  Benchmarks

   -  Motivation: benchmarks are important for efficiency trade-offs.
      Today, there is no clear preferable construction since there are
      many trade-offs to consider.

   -  Proposal example: a specific implementation of a functionality
      (e.g., an agreed-upon arithmetic circuit for SHA256) or by the
      functionality itself (leaving freedom to choose the “most
      friendly” realization thereof).

-  Interoperability

   -  Motivation: many constructions have the ability to use Rank-1
      Constraint Systems and it would be useful to have APIs and file
      formats standardized for interoperability. There is currently a
      mailing list for discussing interoperability of zkp systems and
      implementations.

   -  Proposal example: here is an outline of topics that derived from
      the first workshop, and here is an initial proposal that was
      written.

-  Constructions

   -  Motivation: there are many constructions out there, yet some are
      seeing a lot of adoption and we want to encourage proper usage
      make sure that people are using them correctly. Having a
      standardized specification and test vectors will be beneficial to
      the industry.

   -  Proposal example: see zkp.science for examples of scheme
      constructions and respective implementations.

-  Domain specific languages

   -  Motivation: one of the biggest bottlenecks for using zero
      knowledge systems is the difficulty in writing secure and robust
      constraint systems, for which a DSL would allow more adoption and
      usability.

   -  Proposal example: see zkp.science for examples of DSL’s for
      constraint system generation.

-  Protocols and Applications

   -  Motivation: ensuring that a zkp based system uses a secure
      protocol can be tricky, especially since each one can have
      different privacy requirements or caveats that are not easy to
      detect.

   -  Proposal example: as is outlined in the Applications Track
      proceeding, some (if not most) use-cases share basic requirements
      (confidentiality, anonymity, etc...). Once can use Pedersen Hashes
      or SHA256 for committing to data and use RSA accumulators or
      Merkle TRees for set membership.

For any further questions, please email contact@zkproof.org

16 cm 22 cm -1 cm -0 cm
