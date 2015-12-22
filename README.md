Antelope
===

A modern web framework for creating BitTorrent tracker websites. No assumptions
are made about the content of your tracker, or whether the tracker is open or
private. It truly lets you customise the site to your needs. Antelope is 
written in Python using Django 1.8. By default it uses PostgreSQL for the 
database but can easily be changed with the power of Django.

Antelope also tries to be as modifiable as possible by separating
functionality of the website into different django apps so that you can
easily disable and enable apps as required by your site. The key apps set to be
developed at the moment are: Tracker (uploading/downloading/searching of 
torrents, and user accounts), Forums, Site News Blog. This way if your site 
does not need a forum or a news blog, you can simply disable them.

There is still a lot of work to be done. Please see the TODO to see if you can
help.

###Developing

Docker, docker-compose and docker-machine is used for the development of 
Antelope.

###Code Style

Antelope tries to adhere to [Django's Code Style](https://docs.djangoproject.com/en/1.8/internals/contributing/writing-code/coding-style/``). 
Please follow this style when submitting pull requests. Likewise if you see any
code in the repo which does not conform to those guidelines, please submit a 
fix.
