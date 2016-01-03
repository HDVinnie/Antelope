Configuring Deployment
======================

Antelope is separated into testing and production settings throughout, although
it may suit your needs to add more configurations such as staging and local.
All path files are given relative to the root of the Antelope directory.

Docker
------

The configuration files for Docker are found in the root, and there is a
Dockerfile in `nginx/`. The two main files of concern are the docker-compose
files found in the root: `docker-compose.yml`, and `production.yml`. These files
are responsible for configuring your containers, setting up environment vars
and executing some commands. A good reference for these files is found `here`__.

.. __: https://docs.docker.com/compose/compose-file/

Gunicorn
--------

The configuration files for Gunicorn can be found in `gunicorn/`. Some sane 
defaults are provided but you can read more on how to configure Gunicorn 
`here`__.

.. __: http://docs.gunicorn.org/en/19.4.3/settings.html

The launching of Gunicorn happens in the docker-compose file and it is there
that the appropriate Gunicorn config file is chosen.

Django
------

The main configuration files for Django can be found in 
`antelope/antelope/settings/`. The Django settings are split into a base file, 
`base.py`, and other configurations which build off the base. Something you
may wish to do is to create a local config where you can include your personal
favourite settings that you want to use but don't want to force others to as 
well. This can be done easily by creating a `local.py` file with the following 
example code. Remember to not track this file, and to change the Docker compose
file to use your local settings

.. code-block:: python

  # A personal settings file
  from .testing import *

  INSTALLED_APPS += ("debug_toolbar", )

The Django settings file is chosen in the docker-compose file by setting the
`DJANGO_SETTINGS_MODULE` environment variable.

You will also find in in `antelope/antelope/wsgi.py` a way to set a django 
settings fallback should the above environment variable not be set for any 
reason. The default fallback is to use production settings.

NGINX
-----

The configuration files for NGINX can be found in `nginx/`. At the moment there
is only a server configuration file that is found in `nginx/sites-enabled`.
This config proxies connections to Gunicorn and serves your static files. From
here you will also want to configure any SSL etc.

You may also want a custom nginx.conf which can be easily done by placing one
in `nginx/` and then editing the Dockerfile to include::

  COPY nginx.conf /etc/nginx/nginx.conf

Antelope
--------

To be written once Antelope is more developed. It is planned for you to be able
to change branding, settings (such as open/private), etc. from just one config 
file which will be documented here when ready.
