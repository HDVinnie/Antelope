#Documentation

This directory contains all the documentation for Antelope. 

reStructuredText is used for the markup of doc files, and a Sphinx makefile and 
conf.py is included for building the docs into a HTML website.

You may find the Sphinx generated docs online here: http://astonex.github.io/Antelope/

To build the docs for yourself, you may find it easier to change the BUILDDIR
in the Makefile (or make.bat) which is currently set to update this repo's 
gh-pages branch. To do this, simply change

`BUILDDIR = ../../AntelopeDocs`

to

`BUILDDIR = \_build`

Then you can simply run `make html` to generate your html docs.
