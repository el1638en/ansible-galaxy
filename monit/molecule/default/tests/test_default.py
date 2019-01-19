import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

ansible_vars_path = 'file=../../defaults/main.yml'


def test_host_pkg(host):
    package = host.package('monit')

    assert package.is_installed


def test_monit_running_and_enabled(host):
    monit = host.service('monit')

    assert monit.is_running
    assert monit.is_enabled


def test_monit_config_file(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    monit_config_file = ansible_vars['monit_config_file']

    file = host.file(monit_config_file)
    assert file.exists
    assert oct(file.mode) == '0600'
    assert file.user == 'root'
    assert file.group == 'root'
