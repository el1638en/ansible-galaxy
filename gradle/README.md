gradle
=========

Installation de Gradle(https://gradle.org/).

Requirements
------------

None.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|gradle_version|5.0|Gradle Version|
|gradle_archive_name|gradle-{{gradle_version}}-all.zip|Fichier Archive .zip contenant Gradle|
|gradle_download_archive_url|https://services.gradle.org/distributions/{{gradle_archive_name}}|Url (dynamique) de téléchargement archive|
|gradle_install_directory|/opt/gradle|Repertoire d'installation de Gradle|
|gradle_home|/opt/gradle/gradle-{{gradle_version}}|Chemin absolu d'installation de Gradle|

Dependencies
------------

None.

Example Playbook
----------------

Install gradle

    - hosts: all
      roles:
        - { role: gradle }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
