import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# TODO : Access ansible variable to get lit of package dynamiclly
@pytest.mark.parametrize('pkg', [
    'nfs-common',
    'inetd',
    'portmap',
    'ppp',
    'exim4'
    ])
def test_host_pkg(host, pkg):
    package = host.package(pkg)

    assert not package.is_installed
