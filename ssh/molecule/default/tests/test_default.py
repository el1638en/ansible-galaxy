import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_deleted_obsolete_package(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    for pkgName in ansible_vars['ssh_delete_packages']:
        pkg = host.package(pkgName)
        assert not pkg.is_installed


def test_issue_files(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    ssh_banner_information = ansible_vars['ssh_banner_information']

    for path in ansible_vars['ssh_issue_files']:
        file = host.file(path)
        assert file.exists
        assert file.contains(ssh_banner_information)


def test_motd_file_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    file = host.file(ansible_vars['ssh_motd_file'])
    assert file.exists


def test_package_is_installed(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    ssh_package = host.package(ansible_vars['ssh_package'])
    assert ssh_package.is_installed


def test_banner_file_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    ssh_banner_file_path = ansible_vars['ssh_banner_file']

    file = host.file(ssh_banner_file_path)
    assert file.exists


def test_ssh_config_file(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    ssh_config_file_path = ansible_vars['ssh_config_file']
    file = host.file(ssh_config_file_path)

    for lineConfig in ansible_vars['ssh_config']:
        assert file.contains(lineConfig['value'])
