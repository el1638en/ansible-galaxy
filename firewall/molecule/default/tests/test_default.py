import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ansible_vars_path = 'file=../../defaults/main.yml'


@pytest.mark.parametrize('pkg', [
    'iptables'
    ])
def test_host_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


def test_host_files(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]

    for fileParameter in ansible_vars['firewall_script_files']:
        file = host.file(fileParameter['dest'])
        assert file.exists
        assert oct(file.mode) == fileParameter['mode']


def test_hosts_iptables(host):
    ansible_file = host.ansible("include_vars", ansible_vars_path)
    ansible_vars = ansible_file["ansible_facts"]
    rules = host.iptables.rules()
    input_rules = host.iptables.rules('filter', 'INPUT')
    for line in ansible_vars['firewall_allowed_ports']:
        rule = '-A INPUT -p ' + line['protocol'] + ' -m ' + line['protocol']
        rule = rule + ' --dport ' + line['port']
        rule = rule + ' -m comment --comment "' + line['comment'] + '"'
        rule = rule + ' -j ACCEPT'
        assert rule in rules
        assert rule in input_rules
