========
Overview
========

.. contents::    :depth: 3

Notification server
===================

Debugging
---------

Dump DB counter collection:

::

    mongo notifications-server --eval "c=db.getCollection('counters'); c.find();"

Dump DB notification collection:

::

    mongo notifications-server --eval "c=db.getCollection('notifications'); c.find();"

Get notifications with curl:

::

    curl -XPOST --data '{"idAddr": "0xd9d6800a1b20ceebef5420f878bbd915f8b4ed85"}' "http://127.0.0.1:10000/api/unstable/notifications?afterid=6&beforeid=9" | jq
