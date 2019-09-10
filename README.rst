=============
 toolwrapper
=============

A Python module for interfacing with external text tools.

This module provides a single class `toolwrapper.ToolWrapper`.  Objects of
this class will launch subprocesses and communicate with them via stdin/stdout
pipes.

Copyright ® 2015-2019 Luís Gomes <luismsgomes@gmail.com>.

Changelog
---------

* ``v1.0.0``
    - version bump to reflect actual maturity and stability of this module
    - changed logger name to include the module of the class
* ``v0.4.1``
    - Fixed close()
* ``v0.4.0``
    - added ``LICENSE`` file
    - added tests
    - detect if ``stdbuf`` is available
* ``v0.3.0``
    - changed to MIT license
* ``v0.2.0``
    - moved sources into ./src/ and adjusted setup.py
    - bugfix setup.py
* ``v0.1.0``
    - first working version (unreleased)

