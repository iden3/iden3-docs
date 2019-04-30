=============
Backup Server
=============

.. contents::    :depth: 3

Backup Server
=============

Backup Service
--------------

::

   Wallet                 Backup Service
     +                         +
     |       /register         |
     +------------------------>+
     |        200 OK           |
     +<------------------------+
     |                         |
     |                         |
     |      /backup/upload     |
     +------------------------>+
     |        200 OK           |
     +<------------------------+
     |                         |
     |                         |
     |      /backup/download   |
     +------------------------>+
     |        {backup}         |
     +<------------------------+
     |                         |
     +                         +

Endpoints
~~~~~~~~~

-  POST /register

   -  in:

   .. code:: js

      {
          username: "",
          password: ""
      }

   -  out:

   ::

      200 OK

-  POST /backup/upload

   -  in:

   .. code:: js

      {
          username: "",
          password: ""
          backup: "base64"
      }

   -  out:

   ::

      200 OK

-  POST /backup/download

   -  in:

   .. code:: js

      {
          username: "",
          password: ""
      }

   -  out:

   .. code:: js

      {
          backup: "base64"
      }

-  ERROR

   -  out:

   .. code:: js

      {
          error: "msg"
      }
