import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_host_postgres_packages(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    postgres_server_pkg = host.package(ansible_vars['postgres_server_pkg'])
    postgres_client_pkg = host.package(ansible_vars['postgres_client_pkg'])

    assert postgres_server_pkg.is_installed
    assert postgres_client_pkg.is_installed


def test_postgres_running_and_enabled(host):
    postgresql = host.service('postgresql')

    assert postgresql.is_running
    assert postgresql.is_enabled
