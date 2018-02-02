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
        | |coveralls|
        | |codacy|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/bittrade/badge/?style=flat
    :target: https://readthedocs.org/projects/bittrade
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/JunhaoWang/bittrade.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/JunhaoWang/bittrade

.. |requires| image:: https://requires.io/github/JunhaoWang/bittrade/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/JunhaoWang/bittrade/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/github/JunhaoWang/bittrade/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/github/JunhaoWang/bittrade?branch=master

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/1a92a2df373946789f812c7af01a86e7
    :target: https://www.codacy.com/app/JunhaoWang/bittrade?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JunhaoWang/bittrade&amp;utm_campaign=Badge_Grade
    :alt: Codacy Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/bittrade.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/bittrade

.. |wheel| image:: https://img.shields.io/pypi/wheel/bittrade.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/bittrade

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/bittrade.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/bittrade

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/bittrade.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/bittrade


.. end-badges

Crypto trading AI agent.

* Free software: MIT license

Installation
============

::

    pip install bittrade

Documentation
=============

https://bittrade.readthedocs.io/

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
