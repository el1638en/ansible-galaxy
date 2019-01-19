import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_host_pkg(host):
    package = host.package('ntp')

    assert package.is_installed


def test_ntp_running_and_enabled(host):
    ntp = host.service('ntp')
    assert ntp.is_running
    assert ntp.is_enabled
