Antelope
===

A modern web framework for creating BitTorrent tracker websites. No assumptions
are made about the content of your tracker, or whether the tracker is open or
private. It truly lets you customise the site to your needs. Antelope is 
written in Python using Django 1.8. By default it uses PostgreSQL for the 
database but can easily be changed with the power of Django. It is planned to
utilise Redis for caching stats.

Antelope tries to be as modifiable as possible by separating
functionality of the website into different django apps so that you can
easily disable and enable apps as required by your site. The key apps set to be
developed at the moment are: Torrents (uploading/downloading/searching of 
torrents), Accounts, Forums, Site News Blog. This way if your site 
does not need a forum or a news blog for example, you can simply disable them.

There is still a lot of work to be done. Please see the TODO to see if you can
help.

###Developing

To get started with developing Antelope, please see the instructions here:
http://astonex.github.io/Antelope/installation.html

###Code Style

Antelope tries to adhere to [Django's Code Style](https://docs.djangoproject.com/en/1.8/internals/contributing/writing-code/coding-style/``). 
Please follow this style when submitting pull requests. Likewise if you see any
code in the repo which does not conform to those guidelines, please submit a 
fix.
