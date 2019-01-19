nexus
=========

Installation of nexus repository.

Requirements
------------

JDK.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|nexus_user|nexus|Nexus user|
|nexus_group|nexus|Nexus user group |
|nexus_user_password|nexus|nexus user password|
|nexus_install_directory|/home/nexus|Nexus install directory. It's the homedir of nexus user.|
|nexus_version|2.14.3-02|Nexus version|
|nexus_archive_name|nexus-{{ nexus_version }}-bundle.tar.gz|Nexus archive name|
|nexus_download_archive_url|https://download.sonatype.com/nexus/oss/{{ nexus_archive_name }}|Nexus download URL|
|nexus_home|{{ nexus_install_directory }}/nexus-{{ nexus_version }}|Nexus directory|
|nexus_port|9081|Nexus HTTP port|
|nexus_host|192.168.56.2|Nexus Host IP address|
|nexus_network_interface|eth0|Netwaork interface where iptables rule will be apply.|
|nexus_iptables_enabled|False|If `True`, open `nexus_port` by iptables.|
|nexus_files|{{ nexus_home }}/bin/nexus & {{ nexus_home }}/conf/nexus.properties|Nexus bash script & Nexus configuration properties file|


Dependencies
------------

None.

Example Playbook
----------------

Install maven

    - hosts: servers
      roles:
         - { role: nexus }

License
-------

BSD

Author Information
------------------

Eric LEGBA.
