clean_services
=========

`clean_services` supprime certains packages de base qui sont inutiles.

Requirements
------------

None.

Role Variables
--------------

| Nom	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|remove_services|nfs-common, inetd, portmap, ppp, exim4|Liste des packages à supprimer de l'environnement.|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: clean_services }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
