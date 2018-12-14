import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_apache2_packages_installed(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    apache2_core_packages = ansible_vars['apache2_core_packages']
    apache2_additionnal_packages = ansible_vars['apache2_additionnal_packages']

    for core_package_name in apache2_core_packages:
        core_package = host.package(core_package_name)
        assert core_package.is_installed

    for additionnal_package_name in apache2_additionnal_packages:
        additionnal_package = host.package(additionnal_package_name)
        assert additionnal_package.is_installed


def test_apache2_config_param(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    apache2_config_file_path = ansible_vars['apache2_config_file']
    apache2_config_file = host.file(apache2_config_file_path)

    for lineConfig in ansible_vars['apache2_config_params']:
        assert apache2_config_file.contains(lineConfig['value'])


def test_apache2_config_mods_disabled_not_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    apache2_mods_enabled_dir_path = ansible_vars['apache2_mods_enabled_dir']

    for mod_disabled_config in ansible_vars['apache2_mods_disabled']:
        file = host.file(apache2_mods_enabled_dir_path + '/' + mod_disabled_config + '.conf')
        assert not file.exists


def test_apache2_mods_disabled_not_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    apache2_mods_enabled_dir_path = ansible_vars['apache2_mods_enabled_dir']

    for mod_disabled in ansible_vars['apache2_mods_disabled']:
        file = host.file(apache2_mods_enabled_dir_path + '/' + mod_disabled + '.load')
        assert not file.exists


def test_apache2_mods_enabled_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    apache2_mods_enabled_dir_path = ansible_vars['apache2_mods_enabled_dir']

    for mod_enabled in ansible_vars['apache2_mods_enabled']:
        fileLink = host.file(apache2_mods_enabled_dir_path + '/' + mod_enabled)
        assert fileLink.exists
        assert fileLink.is_symlink


def test_package_python_passlib_is_installed(host):

    python_passlib_package = host.package('python-passlib')
    assert python_passlib_package.is_installed


def test_apache2_status_config_directory_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    status_dir = host.file(ansible_vars['apache2_status_dir'])

    assert status_dir.exists
    assert status_dir.is_directory


def test_apache2_status_authentication_file_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    htpasswd = host.file(ansible_vars['apache2_status_dir'] + '/.htpasswd')

    assert htpasswd.exists
    assert htpasswd.is_file


def test_apache2_status_conf_file_exists(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    status_conf_file = host.file(ansible_vars['apache2_mods_available_dir'] + '/status.conf')
    status_conf_link = host.file(ansible_vars['apache2_mods_enabled_dir'] + '/status.conf')

    assert status_conf_file.exists
    assert status_conf_link.exists
    assert status_conf_link.is_symlink
