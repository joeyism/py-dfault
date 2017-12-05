Dfault
======

A simple lightweight class that allows the user to fallback on default
values

Installation
------------

.. code:: bash

    pip3 install --user dfault

Usage
-----

Basic Example
~~~~~~~~~~~~~

.. code:: python

    from dfault.objects import Dfault

    expected_values = {
                        "search_engine": "duckduckgo",
                        "website": "http://www.duckduckgo.com"
                        }
    d = Dfault(expected_values)
    d.get("search_engine", "google") # returns "duckduckgo" as the value exists
    d.get("favourite_team", "leafs") # returns "leafs" as there are no values for "favourite_team"

With Config
~~~~~~~~~~~

.. code:: python

    import configparser
    from dfault.objects import Dfault

    config = configparser.ConfigParser()

    # .config:
    # [USER]
    # team=leafs
    #
    config.read(".config")
    default_config = config["user"]
    d = Dfault(default_config)
    d.get("team", "raptors") # returns "leafs" as the value exiss in the config
    d.get("username", "joeyism") # returns "joeyism" as there is no "username" value in the config file

Versions
--------

-  **1.0.0**

   -  First Publish
