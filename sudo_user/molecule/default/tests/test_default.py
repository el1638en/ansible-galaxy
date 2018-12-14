import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_user(host):

    user = host.user('test')
    file = host.file('/etc/sudoers.d/test')
    assert user.exists
    assert user.name == "test"
    assert file.exists
