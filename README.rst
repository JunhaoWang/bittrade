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
        | |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/bittrade/badge/?style=flat
    :target: https://readthedocs.org/projects/bittrade
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/JunhaoWang/bittrade.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/JunhaoWang/bittrade

.. |requires| image:: https://requires.io/github/JunhaoWang/bittrade/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/JunhaoWang/bittrade/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/JunhaoWang/bittrade/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/JunhaoWang/bittrade

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/1a92a2df373946789f812c7af01a86e7
    :target: https://www.codacy.com/app/JunhaoWang/bittrade?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JunhaoWang/bittrade&amp;utm_campaign=Badge_Grade
    :alt: Codacy Code Quality Status

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1a92a2df373946789f812c7af01a86e7)]()

.. |codeclimate| image:: https://codeclimate.com/github/JunhaoWang/bittrade/badges/gpa.svg
   :target: https://codeclimate.com/github/JunhaoWang/bittrade
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/bittrade.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/bittrade

.. |commits-since| image:: https://img.shields.io/github/commits-since/JunhaoWang/bittrade/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/JunhaoWang/bittrade/compare/v0.1.0...master

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


.. image:: https://api.codacy.com/project/badge/Grade/eca038aec42840d2b126ec4c239b9e0e
   :alt: Codacy Badge
   :target: https://www.codacy.com/app/JunhaoWang/bittrade?utm_source=github.com&utm_medium=referral&utm_content=JunhaoWang/bittrade&utm_campaign=badger