========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-gem-webcrawl-datafilterer/badge/?version=latest
    :target: https://python-gem-webcrawl-datafilterer.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/DiesDasJenes/python-gem_webcrawl_datafilterer.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/diesdasjenes/python-gem_webcrawl_datafilterer

.. |requires| image:: https://requires.io/github/DiesDasJenes/python-gem_webcrawl_datafilterer/requirements.svg?tag=v0.0.0
     :target: https://requires.io/github/DiesDasJenes/python-gem_webcrawl_datafilterer/requirements/?tag=v0.0.0
     :alt: Requirements Status

.. |codecov| image:: https://codecov.io/gh/diesdasjenes/python-gem_webcrawl_datafilterer/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/diesdasjenes/python-gem_webcrawl_datafilterer

.. |commits-since| image:: https://img.shields.io/github/commits-since/diesdasjenes/python-gem_webcrawl_datafilterer/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/diesdasjenes/python-gem_webcrawl_datafilterer/compare/v0.0.0...master



.. end-badges

The application will filter for actual articles about topics and remove unwanted stuff.

* Free software: BSD 2-Clause License

Installation
============

:: Not yet possible


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
