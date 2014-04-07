Installation
------------

Linux
-----

**Requirements**: ``Lua`` or ``LuaJIT``

Install databuild::

  $ pip install git+https://github.com/fcurella/databuild.git

OS X
----

**Requirements**: ``Lua`` (``LuaJIT`` is not supported ATM)

Temporarily unlink ``LuaJIT`` if you have it installed::

  $ brew unlink luajit

Install ``Lua`` with ``brew``::

  $ brew install lua

Download and extract ``databuild``::

  $ pip install https://github.com/fcurella/databuild/archive/master.tar.gz

After ``databuild`` is installed, you can re-link ``LuaJIT`` if you need::

  $ brew link luajit
