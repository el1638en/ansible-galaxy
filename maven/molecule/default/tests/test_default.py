import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

ansible_vars_path = 'file=../../defaults/main.yml'


def test_maven_install_directory_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    f = host.file(ansible_vars['maven_install_directory'])

    assert f.exists


def test_maven_command(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    mvn_version = ansible_vars['maven_version']
    command = host.run(". /etc/profile && mvn --version 2>&1")

    assert mvn_version in command.stdout
