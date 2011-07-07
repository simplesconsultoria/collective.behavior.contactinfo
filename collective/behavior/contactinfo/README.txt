.. contents:: Table of Contents
   :depth: 2

collective.behavior.contactinfo
*******************************************************************

Overview
--------

This package provides behaviors to deal with contact information.

Available Behaviors
---------------------

Internet contact info
    Providing email, twitter, irc_nickname and site fields

Phone contact Info 
    Providing phone and mobile fields

Requirements
------------

    * Plone >= 4.0.x (http://plone.org/products/plone)
    
    * Dexterity > 1.0 (http://plone.org/products/dexterity)

Installation
------------

To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``collective.behavior.contactinfo``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            collective.behavior.contactinfo

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.


Sponsoring
----------

    * Development of this product was sponsored by:
        
        * `Associacao Python Brasil  <http://associacao.python.org.br/>`_.

        * `Simples Consultoria  <http://www.simplesconsultoria.com.br/>`_.


Credits
-------

    * Simples Consultoria (products at simplesconsultoria dot com dot br) - 
      Implementation

