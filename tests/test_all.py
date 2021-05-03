# pylint: disable=redefined-outer-name,invalid-name
import pytest
from testinfra.host import Host


@pytest.fixture(scope="session")
def target_host(request):
    def fn(host, sudo=True):
        return Host.get_host(
            f"ansible://{host}?ansible_inventory={request.config.option.ansible_inventory}",
            sudo=sudo,
        )

    return fn


def test_borg_binary(host):
    assert host.exists("borg")


def test_borgmatic_binary(target_host):
    host = target_host("client")
    assert host.exists("borgmatic")


def test_config_file(target_host):
    host = target_host("client")
    assert host.file("/etc/borgmatic/config.yaml").exists


def test_run_borgmatic(target_host):
    host = target_host("client")
    result = host.run("borgmatic")
    assert result.succeeded
    assert "Finished backup" in result.stdout


def test_data_dir_created(target_host):
    host = target_host("server")
    assert host.file("/data/nonce").is_file
