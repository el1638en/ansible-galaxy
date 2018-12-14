sudo_user
=========

Ajouter/retirer les droits sudo à un utilisateur.

Requirements
------------

None.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|user_name| - |Nom de l'utilisateur qui recevra les droits sudo.|
|user_comment| - |Commentaire à ajouter à la création de l'utilisateur.|
|user_password|*****|Mot de passe de l'utilisateur|
|user_ssh_key_passphrase|*****|Passphrase de protection de la clé privée de l'utilisateur.|
|user_public_ssh_key|******|Clé publique SSH à ajouter à l'authorized_keys de l'utilisateur|
|user_remove_sudo_right|-|Utilisateur à qui il faut retirer les droits sudo.|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: sudo_users, user_name: "test", user_password: "test", user_public_ssh_key: "ssh-rsa AAAAB3NzaC1*********" }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
