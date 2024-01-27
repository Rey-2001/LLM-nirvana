
import pytest
from packages import bump_version
from packages import *

def test_bump_version_no_change():
    # No change in version when bumping patch position
    assert bump_version('1.2.3') == '1.2.3'
    # No change in version when bumping minor position
    assert bump_version('1.2') == '1.2'
    # No change in version when bumping major position
    assert bump_version('1') == '1'

def test_bump_version_patch_position():
    # Increase patch position by 1
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Increase patch position by 2
    assert bump_version('1.2.3', position=2) == '1.2.4'

def test_bump_version_minor_position():
    # Increase minor position by 1
    assert bump_version('1.2.3', position=1) == '1.3'
    # Increase minor position by 2
    assert bump_version('1.2.3', position=1) == '1.3'

def test_bump_version_major_position():
    # Increase major position by 1
    assert bump_version('1.2.3', position=0) == '2.0'
    # Increase major position by 2
    assert bump_version('1.2.3', position=0) == '2.0'

def test_bump_version_alpha_pre_release():
    # Increase minor pre-release version alpha by 1
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Increase minor pre-release version alpha by 2
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a2'

def test_bump_version_beta_pre_release():
    # Increase minor pre-release version beta by 1
    assert bump_version('1.2.3b0', pre_release='b') == '1.2.3b1'
    # Increase minor pre-release version beta by 2
    assert bump_version('1.2.3b0', pre_release='b') == '1.2.3b2'

def test_bump_version_alpha_pre_release_invalid_position():
    # Trying to bump major part to a pre-release version
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=0, pre_release='alpha')
    # Trying to bump patch part to a pre-release version
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=2, pre_release='alpha')
