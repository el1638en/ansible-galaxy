sonarqube
=========

Installation de SonarQube.

Requirements
------------

None.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|sonarqube_version|6.7|SonarQube version.|
|sonarqube_install_directory|/opt/sonar|SonarQube installation directory.|
|sonarqube_archive_name|sonarqube-{{sonarqube_version}}.zip|SonarQube archive name.|
|sonarqube_download_archive_url|-| URL where download SonarQube archive.|
|sonarqube_home|/opt/sonar/sonarqube-{{sonarqube_version}}|SonarQube home directory.|
|sonarqube_postgres_database_enabled|False|Enable/Disable SonarQube to store its datas into postgres database.|
|sonarqube_postgres_host|localhost|postgres database address.|
|sonarqube_postgres_username|sonar|Postgres database username.|
|sonarqube_postgres_password|sonar|Postgres database password.|
|sonarqube_postgres_database|sonar|Postgres database where sonar will store his datas.|
|sonarqube_postgres_jdbc_url|jdbc:postgresql://{{sonarqube_postgres_host}}/{{ sonarqube_postgres_database }}|Postgres database URL.|
|sonarqube_postgres_config|-|Postgres database config.|
|sonarqube_web_port|9000|SonarQube web port.|
|sonarqube_iptables_enabled|False|If `True`, open `sonarqube_web_port` by iptables.|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sonarqube, x: 42 }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
