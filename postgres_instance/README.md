postgres_instance
=========

Ajout d'instance de base de données, d'utilisateur et de schémas.

Requirements
------------

None.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|dbs|-|List des users, databases et schemas.|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: postgres_instance }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
