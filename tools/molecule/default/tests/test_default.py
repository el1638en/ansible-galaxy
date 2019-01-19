import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_host_pkg(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    for pkgName in ansible_vars['tools_list']:
        pkg = host.package(pkgName)
        assert pkg.is_installed
