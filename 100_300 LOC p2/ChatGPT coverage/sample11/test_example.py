import pytest
import ssl
from ssl_ import HTTPieCertificate, HTTPieHTTPSAdapter, SSL_VERSION_ARG_MAPPING, AVAILABLE_SSL_VERSION_ARG_MAPPING
from ssl_ import *

@pytest.fixture
def adapter():
    return HTTPieHTTPSAdapter(verify=True, ssl_version='tls1.2')

def test_init_poolmanager(adapter):
    assert adapter.ssl_context is not None

def test_init_poolmanager_verify_false():
    adapter = HTTPieHTTPSAdapter(verify=False)
    assert adapter.ssl_context.cert_reqs == ssl.CERT_NONE

def test_init_poolmanager_verify_true():
    adapter = HTTPieHTTPSAdapter(verify=True)
    assert adapter.ssl_context.cert_reqs == ssl.CERT_REQUIRED

def test_init_poolmanager_ssl_version():
    adapter = HTTPieHTTPSAdapter(verify=True, ssl_version='tls1.2')
    assert adapter.ssl_context.protocol == ssl.PROTOCOL_TLSv1_2

def test_init_poolmanager_ssl_version_unknown():
    adapter = HTTPieHTTPSAdapter(verify=True, ssl_version='unknown')
    assert adapter.ssl_context.protocol == ssl.PROTOCOL_SSLv23

def test_init_poolmanager_ciphers_default():
    adapter = HTTPieHTTPSAdapter(verify=True)
    assert adapter.ssl_context.ciphers == DEFAULT_SSL_CIPHERS_STRING

def test_init_poolmanager_ciphers_custom():
    adapter = HTTPieHTTPSAdapter(verify=True, ciphers='AES256-SHA')
    assert adapter.ssl_context.ciphers == 'AES256-SHA'

def test_proxy_manager_for(adapter):
    result = adapter.proxy_manager_for('http://proxy.ssl_.com')
    assert result.ssl_context is not None

def test_cert_verify(cert_file, key_file):
    cert = HTTPieCertificate(cert_file=cert_file, key_file=key_file)
    adapter = HTTPieHTTPSAdapter(verify=True)
    result = adapter.cert_verify(None, 'https://www.ssl_.com', True, cert)
    assert result is not None

def test_cert_verify_no_cert():
    adapter = HTTPieHTTPSAdapter(verify=True)
    result = adapter.cert_verify(None, 'https://www.ssl_.com', True, None)
    assert result is None

def test_cert_verify_encrypted_key_file(key_file_encrypted):
    cert = HTTPieCertificate(key_file=key_file_encrypted)
    adapter = HTTPieHTTPSAdapter(verify=True)
    result = adapter.cert_verify(None, 'https://www.ssl_.com', True, cert)
    assert result is not None

def test_is_key_file_encrypted(key_file, key_file_encrypted):
    assert _is_key_file_encrypted(key_file) is False
    assert _is_key_file_encrypted(key_file_encrypted) is True

def test_ssl_version_args():
    assert AVAILABLE_SSL_VERSION_ARG_MAPPING['tls1.2'] == ssl.PROTOCOL_TLSv1_2
    assert AVAILABLE_SSL_VERSION_ARG_MAPPING.get('unknown') is None

def test_get_default_ciphers_names():
    assert len(HTTPieHTTPSAdapter.get_default_ciphers_names()) > 0

def test_to_raw_cert(cert_file, key_file):
    cert = HTTPieCertificate(cert_file=cert_file, key_file=key_file)
    result = cert.to_raw_cert()
    assert len(result) == 2
    assert result[0] == cert.cert_file
    assert result[1] == cert.key_file

def _is_key_file_encrypted(key_file):
    """Detects if a key file is encrypted or not.

    Copy of the internal urllib function (urllib3.util.ssl_)"""

    with open(key_file, "r") as f:
        for line in f:
            # Look for Proc-Type: 4,ENCRYPTED
            if "ENCRYPTED" in line:
                return True

    return False

def test_is_key_file_encrypted(key_file, key_file_encrypted):
    assert _is_key_file_encrypted(key_file) is False
    assert _is_key_file_encrypted(key_file_encrypted) is True