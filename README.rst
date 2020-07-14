========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-gem_webcrawl_datafilterer/badge/?style=flat
    :target: https://readthedocs.org/projects/python-gem_webcrawl_datafilterer
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/diesdasjenes/python-gem_webcrawl_datafilterer.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/diesdasjenes/python-gem_webcrawl_datafilterer

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/diesdasjenes/python-gem_webcrawl_datafilterer?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/diesdasjenes/python-gem_webcrawl_datafilterer

.. |requires| image:: https://requires.io/github/diesdasjenes/python-gem_webcrawl_datafilterer/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/diesdasjenes/python-gem_webcrawl_datafilterer/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/diesdasjenes/python-gem_webcrawl_datafilterer/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/diesdasjenes/python-gem_webcrawl_datafilterer

.. |version| image:: https://img.shields.io/pypi/v/gem-webcrawl-datafilterer.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/gem-webcrawl-datafilterer

.. |wheel| image:: https://img.shields.io/pypi/wheel/gem-webcrawl-datafilterer.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/gem-webcrawl-datafilterer

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/gem-webcrawl-datafilterer.svg
    :alt: Supported versions
    :target: https://pypi.org/project/gem-webcrawl-datafilterer

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/gem-webcrawl-datafilterer.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/gem-webcrawl-datafilterer

.. |commits-since| image:: https://img.shields.io/github/commits-since/diesdasjenes/python-gem_webcrawl_datafilterer/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/diesdasjenes/python-gem_webcrawl_datafilterer/compare/v0.0.0...master



.. end-badges

The application will filter for actual articles about topics and remove unwanted stuff.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install gem-webcrawl-datafilterer

You can also install the in-development version with::

    pip install https://github.com/diesdasjenes/python-gem_webcrawl_datafilterer/archive/master.zip


Documentation
=============


https://python-gem_webcrawl_datafilterer.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
