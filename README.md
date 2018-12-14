# ansible-galaxy

## Introduction

Ansible est un logiciel open-source écrit en Python dédié au déploiement et à la configuration de serveurs à distance. Il permet d'automatiser les tâches récurrentes de déploiement et d'administration système. Ces tâches répétitives sont écrites dans des fichiers YAML appelés *playbooks*. C'est le contenu des *playbooks* qu'Ansible exécute sur les serveurs distants.

Les avantages d'Ansible sont son idempotence et sa capacité à déployer plusieurs serveurs (groupe d'hôtes) simultanément sans aucun agent de déploiement.
Ansible n'utilise pas de clients, ni d'agents sur les serveurs hôtes distants. Il nécessite une machine disposant d'un système Linux. Depuis cette machine («la tour de contrôle», la machine sur laquelle Ansible est installé), Ansible utilise le protocole *SSH* pour se connecter aux serveurs distants et exécute les *playbooks*.

## Installation

1. Environnement

Nous installons Ansible sur une machine Debian 9.5

```
root@vm-debian-1:~# uname -a
Linux vm-debian-1 4.9.0-7-amd64 #1 SMP Debian 4.9.110-3+deb9u2 (2018-08-13) x86_64 GNU/Linux

root@vm-debian-1:~# lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 9.5 (stretch)
Release:        9.5
Codename:       stretch
```

2. Pré-requis

    1. Mettre à jour l'Environnement

    ```
    root@vm-debian-1:~# apt update
    ```

    2. Installer le package `python-pip`

    ```
    root@vm-debian-1:~# apt install -y python-pip
    ```

    3. Installer les packages `virtualenv` et `virtualenvwrapper`

    ```
    root@vm-debian-1:~# pip install virtualenv virtualenvwrapper
    ```

      - `virtualenv` permet de créer des environnements virtuels Python dans lesquels on pourra exécuter du code Ansible.
      - `virtualenvwrapper` permet de changer d’environnement virtuel facilement.

    4. Ajouter les lignes ci-dessous dans votre fichier `~/.bashrc`

    ```
    export WORKON_HOME=~/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
    mkdir -p $WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh
    ```

      Si les chemins absolus de `python`, `virtualenv`, `virtualenvwrapper.sh` sont différents sur votre machine, il convient de modifier les lignes de codes ci-dessus.

      Fermer votre terminal Shell et relancer de nouveau. Plusieurs lignes vont s’afficher. Pas d’inquiétude, cela n’arrive qu’une seule fois pour initialiser les commandes nécessaires au travail dans un environnement virtuel.

      Voici quelques commandes pour gérer les environnements virtuels :

      - créer un environnement virtuel nommé `nom_env` : utiliser la commande `mkvirtualenv`

        ```
        legeric@vm-debian-1:~# mkvirtualenv nom_env
        ```

      - activer l’environnement virtuel `nom_env` : utiliser la commande `workon`

        ```
        legeric@vm-debian-1:~# workon nom_env
        (nom_env) root@vm-debian-1:~#
        ```

      - quitter l’environnement virtuel : utiliser la commande `deactivate`

        ```
        (nom_env) legeric@vm-debian-1:~# deactivate
        root@vm-debian-1:~#
        ```

      - supprimer l’environnement virtuel `nom_env` : utiliser la commande `rmvirtualenv`

         ```
         legeric@vm-debian-1:~# rmvirtualenv nom_env
         ```

      - connaître la liste des environnements virtuels : utiliser la commande `lsvirtualenv`

          ```
          legeric@vm-debian-1:~# lsvirtualenv
          ```

3. Installation d'Ansible

    1. Créer un environnement virtuel et l'activer

      ```
      legeric@vm-debian-1:~# mkvirtualenv my_env
      ```

    2. Installer `molecule`

      Au lieu d’installer Ansible dans notre environnement virtuel (`pip install ansible`), nous allons installer le package `molecule` qui est un outil de test de code Ansible. En installant le package `molecule`, celui-ci installe automatiquement `Ansible` dans l'environnement virtuel.

      ```
      (my_env)legeric@vm-debian-1:~# pip install molecule
      (my_env)legeric@vm-debian-1:~# molecule --version
      molecule, version 2.19.0
      (my_env)legeric@vm-debian-1:~# ansible --version
      ansible 2.7.1
      config file = None
      configured module search path = [u'/home/legeric/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
      ansible python module location = /home/legeric/.virtualenvs/my_env/local/lib/python2.7/site-packages/ansible
      executable location = /home/legeric/.virtualenvs/my_env/bin/ansible
      python version = 2.7.13 (default, Sep 26 2018, 18:42:22) [GCC 6.3.0 20170516]
      ```

    3. Installer `docker`

      Docker est une librairie Python qui permet de gérer l’interface entre `molecule` et `docker`.

      ```
      (my_env)legeric@vm-debian-1:~# pip install docker
      (my_env)legeric@vm-debian-1:~# docker --version
      Docker version 18.06.1-ce, build e68fc7a
      ```
