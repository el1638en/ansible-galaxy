import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_openjdk_package_is_installed(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    assert host.package(ansible_vars['openjdk_package']).is_installed


def test_java_command_is_up(host):

    command = host.run(". /etc/environment && java -version 2>&1")

    assert "1.8" in command.stdout
