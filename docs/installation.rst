Installation
------------

Install databuild::

  $ pip install git+https://github.com/fcurella/databuild.git

Lua Support
===========

In order to be able to use Lua, you'll need to have the Lua environment
installed before you install ``databuild``.

Linux
~~~~~

**Requirements**: ``Lua`` or ``LuaJIT``

On Ubuntu, these are the packages you need::

  $ sudo apt-get install liblua5.1-0-dev liblua50-dev liblualib50-dev

Then you can install ``databuild``::

  $ pip install https://github.com/fcurella/databuild/archive/master.tar.gz


OS X
~~~~

**Requirements**: ``Lua`` (``LuaJIT`` is not supported ATM)

Temporarily unlink ``LuaJIT`` if you have it installed::

  $ brew unlink luajit

Install ``Lua`` with ``brew``::

  $ brew install lua

Install ``databuild`` with the `WITHLUA` environment variable set::

  $ WITHLUA=True pip install https://github.com/fcurella/databuild/archive/master.tar.gz

After ``databuild`` is installed, you can re-link ``LuaJIT`` if you need::

  $ brew link luajit
