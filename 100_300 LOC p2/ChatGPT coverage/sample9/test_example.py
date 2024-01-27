
import pytest
from config import read_raw_config, Config
from config import *

@pytest.fixture
def config_path(tmp_path):
    return tmp_path / 'config.json'


def test_read_raw_config_invalid_file(config_path):
    with pytest.raises(Exception, match='invalid config file'):
        path = config_path.resolve()
        read_raw_config('config', path)


def test_read_raw_config_file_not_found(config_path):
    assert read_raw_config('config', config_path.resolve()) is None


def test_config_default_options(config_path):
    config = Config(config_path)
    assert config.default_options == []


def test_config_plugins_dir(config_path):
    config = Config(config_path)
    assert config.plugins_dir == config.directory / 'plugins'


def test_config_version_info_file(config_path):
    config = Config(config_path)
    assert config.version_info_file == config.directory / 'version_info.json'


def test_config_developer_mode(config_path):
    config = Config(config_path)
    assert not config.developer_mode


def test_config_save_load(config_path):
    config = Config(config_path)
    config.default_options = ['-v']
    config.save()

    new_config = Config(config_path)
    new_config.load()
    assert new_config.default_options == ['-v']
