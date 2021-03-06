import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


def test_admin_tools_files(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    for line in ansible_vars['admin_tools_files']:
        file = host.file(line['dest'])
        assert file.exists
        assert oct(file.mode) == '0755'
        assert file.user == 'root'
        assert file.group == 'root'
