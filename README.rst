little-pwny
***********

Check whether a given passphrase has been compromised

|bdg-build| \| |pypi-release|


`little-pwny` queries the `have-i-been-pwned password database
<https://haveibeenpwned.com/Passwords>`_ for breaches that contain a given
passphrase and returns the number of breaches found. It does *not* reveal the
plain passphrase to the database (nor to any other party, see below).

`little-pwny` works with plain Python 3.x and requires no additional packages.


Usage
=====

::

    $ pwny p@ssw0rd
    51763

    $ pwny aiPh1eehec8AhY2y
    0

Use::

    $ pwny --help

to learn more about all options supported.

Please note, that the Python package is called `little-pwny` while the
executable script is called `pwny`.

At no time the raw password is transferred to https://haveibeenpwned.com.
Instead we use the generously offered haveibeenpwned.com-API to deploy
`k-anonymity <https://en.wikipedia.org/wiki/K-anonymity>`_. I.e. we send the
first five chars of the SHA1 hash of any given password. This way you can check
new passwords without revealing them to the server (or any other party).



Install
=======

with `pip`
----------

Simply::

    $ pip install little-pwny


From Source
-----------

Clone the source::

     $ git clone https://github.com/ulif/little-pwny
     $ cd little-pwny

Create and activate a virtualenv::

     $ virtualenv venv
     $ source ./venv/bin/activate.sh

Then, from this directory, install the package::

     [venv] $ pip install -e .


Running Tests
=============

We use `tox` and `py.test` for testing. So,::

     $ pip install tox
     $ tox

should run all tests.

.. |bdg-build| image:: https://travis-ci.org/ulif/little-pwny.svg?branch=master
   :target: https://travis-ci.org/ulif/little-pwny
   :alt: Build Status

.. |pypi-release| image:: https://img.shields.io/pypi/v/little-pwny?color=006dad
   :target: https://pypi.python.org/pypi/little-pwny/
   :alt: Latest release
