openjdk
=========

Installation du package Open JDK.

Requirements
------------

None.

Role Variables
--------------

| Name	        | Default Value	| Description|
| ------------- |:-------------:| ----------:|
|openjdk_package|openjdk-8-jdk|Version d'openjdk.|

Dependencies
------------

None.

Example Playbook
----------------

- hosts: servers
  roles:
     - { role: openjdk }

License
-------

BSD

Author Information
------------------

Eric Coovi LEGBA.
