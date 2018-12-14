firewall
=========

Le rôle `firewall` installe un par-feu basé sur `iptables`.

Requirements
------------

None.

Role Variables
--------------

| Nom	        | Valeur par défaut	| Description|
| ------------- |:-------------:| ----------:|
|firewall_daemon_script|/etc/systemd/system/firewall.service|Script SystemD pour contrôler le démarrage/l'arrêt/le re-démarrage du service `firewall`.|
|firewall_script_files| /etc/firewall.bash & /etc/systemd/system/firewall.service |Liste des fichiers de configuration du service `firewall`.|
|firewall_allowed_ports| - |Liste des ports à ouvrir.|
|firewall_forwarded_ports| - |Liste des ports auxquels il faut appliquer la politique FORWARD.|
|firewall_additional_rules| - |Liste des règles additionnelles IPV4.|
|firewall_ip6_additional_rules| - |Liste des règles additionnelles IPv6.|
|firewall_log_dropped_packets| true | Logger la liste des packets détruits par le service `firewall`.|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: firewall }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
