apache2
=========

Installation et configuration du serveur Apache2.

Requirements
------------

None.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|apache2_port|80|Port d'écoute d'Apache2.|
|apache2_config_dir|/etc/apache2|Repertoire des fichiers de configuration Apache2.|
|apache2_config_file|{{ apache2_config_dir }}/apache2.conf|Fichier de configuration Apache2.|
|apache2_mods_available_dir|{{ apache2_config_dir }}/mods-available|Répertoire des modules Apache2 disponibles.|
|apache2_mods_enabled_dir|{{ apache2_config_dir }}/mods-enabled|Répertoire des modules Apache2 activés.|
|apache2_mods_disabled|[]|Liste des modules Apache2 à désactiver.|
|apache2_mods_enabled|[]|Liste des modules Apache2 à activer.|
|apache2_config_params|[]|Liste des directives de configuration.|
|apache2_mod_security_dir|/etc/modsecurity|Répertoire de configuration d'Apache2 Modsecurity.|
|apache2_mod_security_config|[]|Liste des directives de configuration de Modsecurity.|
|apache2_status_dir|[]|Liste des directives de configuration de Modsecurity.|
|apache2_mod_security_config|[]|Liste des directives de configuration de Modsecurity.|
|apache2_status_dir|/var/www/status|Répertoire du VirtualHost status.|
|apache2_status_server_name|À renseigner|Adresse du virtualhost status.|
|apache2_status_server_alias|À renseigner|Alias du virtualhost status.|
|apache2_status_require_ip|-|Adresse IP autorisée à accéder au virtualhost status.|
|apache2_status_require_host|-|Nom du hôte autorisé à accéder au virtualhost status.|
|apache2_server_admin|root@admin|Mail de l'admin du serveur (à réécrire/override).|
|apache2_status_auth_login|EL1638EN|Login d'accès au virtualhost (à réécrire/override).|
|apache2_status_auth_passowrd|Mmdp-3325|LMot de passe d'accès au virtualhost (à réécrire/override).|


Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: apache2 }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
