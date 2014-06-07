.. _expressions:

Expressions
===========

Expressions are objects encapsulating code for situations such as filtering or calculations.

An expression has the following properties:

* ``language``: The name of the environment where the expression will be executed, as specified in ``settings.LANGUAGES``. See :ref:`languages-setting`).
* ``content``: The actual code to run, or
* ``path``: path to a file containing the code to run

The expression will be evaluated inside a function and run against every row in the datasheet. The following context variables will be avalaible::

* ``row``: A dictionary representing the currently selected row.
