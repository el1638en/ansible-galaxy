admin_tools
=========

Le rôle `admin_tools` ajoute des scripts shell d'admin accessibles au super-user root.
Ces commandes permettent d'effectuer facilement certaines tâches (création d'une bdd, d'un utilisateur,
de clé SSH, etc...)

Requirements
------------

None

Role Variables
--------------

| Nom	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|admin_tools_files|pg_tools, ssh_key_tools, user_tools|Liste des scripts shell à ajouter à l'environnement.|

Dependencies
------------

None.

Example Playbook
----------------

  - hosts: servers
    roles:
       - { role: admin_tools }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
