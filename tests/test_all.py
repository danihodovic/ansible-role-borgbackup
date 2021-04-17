def test_borg_binary(host):
    assert host.exists("borg")


def test_borgmatic_binary(host):
    assert host.exists("borgmatic")


def test_config_file(host):
    assert host.file("/etc/borgmatic/config.yaml").exists


def test_run_borgmatic(host):
    result = host.run("borgmatic")
    assert result.succeeded
    assert "Finished backup" in result.stdout
