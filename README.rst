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
        | |coveralls|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/bittrade/badge/?style=flat
    :target: https://readthedocs.org/projects/bittrade
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/JunhaoWang/bittrade.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/JunhaoWang/bittrade

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/JunhaoWang/bittrade?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/JunhaoWang/bittrade

.. |requires| image:: https://requires.io/github/JunhaoWang/bittrade/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/JunhaoWang/bittrade/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/JunhaoWang/bittrade/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/JunhaoWang/bittrade

.. |landscape| image:: https://landscape.io/github/JunhaoWang/bittrade/master/landscape.svg?style=flat
    :target: https://landscape.io/github/JunhaoWang/bittrade/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://www.codacy.com/app/JunhaoWang/bittrade
    :alt: Codacy Code Quality Status

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

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/JunhaoWang/bittrade/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/JunhaoWang/bittrade/


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