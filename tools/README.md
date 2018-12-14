tools
=========

Installation de packages quasi-incontournables.

Requirements
------------

None.

Role Variables
--------------

| Nom	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|tools_list|git, vim, curl, openssl, sudo, sshpass, python-pip, certbot|Liste des packages à supprimer de l'environnement.|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: tools }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
