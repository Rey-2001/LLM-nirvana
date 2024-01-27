
import pytest
from sessions import Session, strip_port, is_anonymous_session
from sessions import *
def test_strip_port():
    # Test cases for the strip_port() function
    assert strip_port("sessions.com:8080") == "sessions.com"
    assert strip_port("localhost") == "localhost"
    assert strip_port("127.0.0.1:8000") == "127.0.0.1"

def test_is_anonymous_session():
    # Test cases for the is_anonymous_session() function
    assert is_anonymous_session("~/.httpie/sessions/session.json") == True
    assert is_anonymous_session("sessions.com_session") == False
    assert is_anonymous_session("session") == False

def test_session_init():
    # Test case for initializing a session object
    session = Session("~/.httpie/sessions/session.json", env=MockEnvironment(), bound_host="sessions.com", session_id="session")
    assert session.path == Path("~/.httpie/sessions/session.json")
    assert session.env == MockEnvironment()
    assert session.session_id == "session"
    assert session.bound_host == "sessions.com"
    assert session.suppress_legacy_warnings == False

def test_update_headers():
    # Test case for updating session headers
    session = Session("~/.httpie/sessions/session.json", env=MockEnvironment(), bound_host="sessions.com", session_id="session")
    headers = {"Content-Type": "application/json"}
    session.update_headers(headers)
    assert session.headers == {"Content-Type": "application/json"}

def test_auth_setter():
    # Test case for setting the session auth
    session = Session("~/.httpie/sessions/session.json", env=MockEnvironment(), bound_host="sessions.com", session_id="session")
    session.auth = {"type": "basic", "raw_auth": "username:password"}
    assert session.auth == AuthBase()

def test_is_anonymous():
    # Test case for checking if the session is anonymous
    session = Session("~/.httpie/sessions/session.json", env=MockEnvironment(), bound_host="sessions.com", session_id="~/.httpie/sessions/session.json")
    assert session.is_anonymous == True

class MockEnvironment:
    def log_error(self, message, level):
        pass

