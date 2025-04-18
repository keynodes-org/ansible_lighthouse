import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")

@pytest.mark.parametrize(
    "directory",
    [
        "/opt/lighthouse/data",
        "/opt/lighthouse/config",
        "/opt/lighthouse/logs"
    ]
)
def test_directories(host, directory):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == "lighthouse"
    assert d.group == "lighthouse"

@pytest.mark.parametrize(
    "file",
    [
        "/usr/local/bin/lighthouse",
        "/opt/lighthouse/config/jwt.hex"
    ],
)
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file

def test_service_file(host):
    # Test the appropriate service file based on mode
    service_name = "lighthouse-beacon"
    f = host.file(f"/lib/systemd/system/{service_name}.service")
    assert f.exists
    assert f.is_file
    assert f.user == "lighthouse"

def test_jwt_file_permissions(host):
    f = host.file("/opt/lighthouse/config/jwt.hex")
    assert f.exists
    assert f.is_file
    assert f.user == "lighthouse"
    assert f.group == "lighthouse"
    assert f.mode == 0o640  # Check restrictive permissions

def test_lighthouse_user(host):
    u = host.user("lighthouse")
    assert u.exists
    assert u.group == "lighthouse"
    assert u.shell == "/usr/sbin/nologin"


def test_lighthouse_binary(host):
    cmd = host.run("/usr/local/bin/lighthouse --version")
    assert cmd.rc == 0
    assert "Lighthouse" in cmd.stdout


@pytest.mark.parametrize("service", ["lighthouse-beacon"])
def test_service(host, service):
    s = host.service(service)
    assert s.is_running
    assert s.is_enabled
