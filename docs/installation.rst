Installation
============

Here are the instructions for setting up Antelope ready for development

Requirements
------------

The required packages for setting up Antelope are::

    docker, docker-compose, docker-machine, virtualbox

The exact installation process for your OS may differ but below are the
instructions needed for installing on Arch Linux. For other Linux distributions
all you may have to do is simply change the package manager.

If docker-machine is not available in your distributions repositories, you will
find releases on Docker's Github (as is done below). Additional installation
instructions can also be found `here`_.

.. _here: https://docs.docker.com/machine/

::

    $ sudo pacman -S docker, docker-compose, virtualbox
    $ curl -L https://github.com/docker/machine/releases/download/v0.5.5/docker-machine_linux-amd64 >/usr/local/bin/docker-machine && \
        chmod +x /usr/local/bin/docker-machine

Creating a development virtual machine
--------------------------------------

The next step is to setup a virtual machine to deploy to using docker-machine::

    $ docker-machine create -d virtualbox dev

This will create a virtual machine named 'dev'. Next you need to set the correct
environment vars for docker-compose. This can be done like so::

    $ eval "$(docker-machine env dev)"

If docker-machine is complaining about not being able to connect to your machine
you may have to run the following command::

    $ sudo dhcpcd vboxnet0

'vboxnet0' is the interface created by virtualbox for your dev machine. This 
should be the same name for you but you can double check using::

    $ ip addr

Deploying to your development machine
-------------------------------------

In the root of the Antelope directory is a file called 'buildtesting.sh'. By
running this script it will build your containers using docker-compose. The 
first time you run this command, it will take a while to download all the
requirements but they do get cached for future uses.

Once done, you should be able to visit Antelope in your browser using the IP
given to your development mahcine::

    $ docker-machine ip dev
