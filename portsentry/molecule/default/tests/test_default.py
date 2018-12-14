import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'portsentry'
    ])
def test_host_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


# TODO : Access ansible variable to get file dynamiclly
@pytest.mark.parametrize('path, mode', [
  ("/etc/portsentry/portsentry.conf", "0644"),
  ("/etc/portsentry/portsentry.ignore.static", "0644"),
  ("/etc/portsentry/notification.sh", "0755")
])
def test_host_files(host, path, mode):
    file = host.file(path)

    assert file.exists
    assert oct(file.mode) == mode
