import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

ansible_vars_path = 'file=../../defaults/main.yml'


def test_gradle_install_directory_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    f = host.file(ansible_vars['gradle_install_directory'])

    assert f.exists
