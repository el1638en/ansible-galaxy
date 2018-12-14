postgres
=========

Installation du serveur de BDD PostgreSQL.

Requirements
------------

None.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|postgres_version|9.4|Version du serveur PostgreSQL.|
|postgres_server_pkg|postgresql-9.4|Package du serveur PostgreSQL.|
|postgres_client_pkg|postgresql-client-9.4|Package PSQL client.|

Dependencies
------------
None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: postgres }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
