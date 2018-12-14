import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_host_pkg(host):
    package = host.package('fail2ban')

    assert package.is_installed


def test_fail2ban_running_and_enabled(host):
    fail2ban = host.service('fail2ban')
    
    assert fail2ban.is_running
    assert fail2ban.is_enabled
