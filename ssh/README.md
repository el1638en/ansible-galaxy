ssh
=========

Installation & configuration de `ssh`.

Requirements
------------

None.

Role Variables
--------------

| Nom	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|ssh_delete_packages|telnet, rshd, rlogin|Liste des packages à supprimer de l'environnement.|
|ssh_package|openssh-server|Nom du package du serveur `ssh`.|
|ssh_banner_information|Linux SSH Server|SSH Banner information.|
|ssh_tmout|900|Après 900 secondes d'inactivité, la connexion `ssh` est désactivée.|
|ssh_histsize|20|Taille de l'historique des commandes|
|ssh_histfilesize|20|Taille du fichier contenant l'historique des commandes|
|ssh_motd_file|/etc/motd|The Message Of The Day.|
|ssh_banner_file|/etc/ssh/ssh_banner|`ssh` Banner.|
|ssh_profile_file|/etc/profile|Fichier de configuration de profil.|
|ssh_config_port|22|Port TCP du serveur `ssh`.|
|ssh_config_file|/etc/ssh/sshd_config|Fichier de configuration `ssh`.|
|ssh_config|-|List des directives de configuration du serveur `ssh`.|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ssh }

License
-------
BSD

Author Information
------------------
Eric LEGBA.
