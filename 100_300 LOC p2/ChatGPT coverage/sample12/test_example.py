
import pytest
import httpie.uploads
from httpie.uploads import *

@pytest.fixture
def environment():
    env = uploads.Environment()
    env.stderr = []
    return env


def test_chunked_upload_stream_iter():
    def callback(chunk):
        pass

    stream = [b'chunk1', b'chunk2', b'chunk3']
    chunked_stream = uploads.ChunkedUploadStream(stream=stream, callback=callback)

    result = list(chunked_stream)
    assert result == stream


def test_chunked_multipart_upload_stream_iter():
    encoder_data = uploads.MultipartRequestDataDict()
    encoder_data.add_field('field1', 'value1')
    encoder_data.add_field('field2', 'value2')
    encoder = uploads.get_multipart_data_and_content_type(encoder_data)

    chunked_stream = uploads.ChunkedMultipartUploadStream(encoder=encoder)

    result = list(chunked_stream)
    assert result == list(encoder)


def test_as_bytes_for_str_input():
    assert uploads.as_bytes("string") == b"string"


def test_as_bytes_for_byte_input():
    assert uploads.as_bytes(b"string") == b"string"


def test_wrap_function_with_callback():
    def func():
        return b"result"

    def callback(chunk):
        assert chunk == b"result"

    wrapped_func = uploads._wrap_function_with_callback(func, callback)

    result = wrapped_func()
    assert result == b"result"


def test_is_stdin_with_valid_stdin():
    assert uploads.is_stdin(sys.stdin) == True


def test_is_stdin_with_invalid_stdin():
    assert uploads.is_stdin(sys.stdout) == False


def test_observe_stdin_for_data_thread_with_threshold():
    env = environment()
    file = sys.stdin
    read_event = uploads.threading.Event()
    uploads.observe_stdin_for_data_thread(env, file, read_event)

    assert len(env.stderr) == 0


def test_observe_stdin_for_data_thread_without_threshold():
    env = environment()
    file = sys.stdin
    read_event = uploads.threading.Event()
    uploads.READ_THRESHOLD = 0
    uploads.observe_stdin_for_data_thread(env, file, read_event)

    assert len(env.stderr) == 0


def test_read_file_with_selectors_with_valid_file():
    file = open("test.txt", "w")
    file.write("test")
    file.close()
    file = open("test.txt", "r")
    read_event = uploads.threading.Event()

    result = uploads._read_file_with_selectors(file, read_event)
    assert result == b"test"


def test_read_file_with_selectors_with_invalid_file():
    file = sys.stdout
    read_event = uploads.threading.Event()

    result = uploads._read_file_with_selectors(file, read_event)
    assert result == b""


def test_prepare_file_for_upload_with_file_like_and_non_zero_length():
    env = environment()
    file = uploads.open("test.txt", "w")
    file.write("test")
    file.close()
    file = uploads.open("test.txt", "r")
    callback = lambda chunk: None
    chunked = False
    content_length_header_value = None

    result = uploads._prepare_file_for_upload(env, file, callback, chunked, content_length_header_value)
    assert result == file


def test_prepare_file_for_upload_with_file_like_and_zero_length():
    env = environment()
    file = sys.stdin
    callback = lambda chunk: None
    chunked = False
    content_length_header_value = None

    result = uploads._prepare_file_for_upload(env, file, callback, chunked, content_length_header_value)
    assert result == b""


def test_prepare_file_for_upload_with_chunked_and_encoder():
    env = environment()
    encoder_data = uploads.MultipartRequestDataDict()
    encoder_data.add_field('field1', 'value1')
    encoder_data.add_field('field2', 'value2')
    encoder = uploads.get_multipart_data_and_content_type(encoder_data)
    chunked = True
    content_length_header_value = None

    result = uploads._prepare_file_for_upload(env, encoder, callback=lambda chunk: None, chunked=chunked, content_length_header_value=content_length_header_value)
    assert isinstance(result, uploads.ChunkedMultipartUploadStream)


def test_prepare_file_for_upload_with_chunked_and_stream():
    env = environment()
    stream = [b'chunk1', b'chunk2', b'chunk3']
    chunked = True
    content_length_header_value = None

    result = uploads._prepare_file_for_upload(env, stream, callback=lambda chunk: None, chunked=chunked, content_length_header_value=content_length_header_value)
    assert isinstance(result, uploads.ChunkedUploadStream)


def test_prepare_file_for_upload_with_not_chunked():
    env = environment()
    file = uploads.open("test.txt", "w")
    file.write("test")
    file.close()
    file = uploads.open("test.txt", "r")
    callback = lambda chunk: None
    chunked = False
    content_length_header_value = None

    result = uploads._prepare_file_for_upload(env, file, callback, chunked, content_length_header_value)
    assert result == file


def test_prepare_request_body_with_str_input():
    env = environment()
    raw_body = "request body"
    body_read_callback = lambda chunk: None
    offline = False
    chunked = False
    content_length_header_value = None

    result = uploads.prepare_request_body(env, raw_body, body_read_callback, offline, chunked, content_length_header_value)
    assert result == b"request body"


def test_prepare_request_body_with_byte_input():
    env = environment()
    raw_body = b"request body"
    body_read_callback = lambda chunk: None
    offline = False
    chunked = False
    content_length_header_value = None

    result = uploads.prepare_request_body(env, raw_body, body_read_callback, offline, chunked, content_length_header_value)
    assert result == b"request body"


def test_prepare_request_body_with_dict_input():
    env = environment()
    raw_body = {"field1": "value1", "field2": "value2"}
    body_read_callback = lambda chunk: None
    offline = False
    chunked = False
    content_length_header_value = None

    result = uploads.prepare_request_body(env, raw_body, body_read_callback, offline, chunked, content_length_header_value)
    assert result == b"field1=value1&field2=value2"


def test_prepare_request_body_with_file_like_input_and_offline_false():
    env = environment()
    file = uploads.open("test.txt", "w")
    file.write("test")
    file.close()
    file = uploads.open("test.txt", "r")
    body_read_callback = lambda chunk: None
    offline = False
    chunked = False
    content_length_header_value = None

    result = uploads.prepare_request_body(env, file, body_read_callback, offline, chunked, content_length_header_value)
    assert result == file


def test_prepare_request_body_with_file_like_input_and_offline_true():
    env = environment()
    file = uploads.open("test.txt", "w")
    file.write("test")
    file.close()
    file = uploads.open("test.txt", "r")
    body_read_callback = lambda chunk: None
    offline = True
    chunked = False
    content_length_header_value = None

    result = uploads.prepare_request_body(env, file, body_read_callback, offline, chunked, content_length_header_value)
    assert result == b"test"


def test_prepare_request_body_with_chunked_true():
    env = environment()
    raw_body = "request body"
    body_read_callback = lambda chunk: None
    offline = False
    chunked = True
    content_length_header_value = None

    result = uploads.prepare_request_body(env, raw_body, body_read_callback, offline, chunked, content_length_header_value)
    assert isinstance(result, uploads.ChunkedUploadStream)


def test_prepare_request_body_with_content_length_header_value():
    env = environment()
    raw_body = "request body"
    body_read_callback = lambda chunk: None
    offline = False
    chunked = False
    content_length_header_value = 10

    result = uploads.prepare_request_body(env, raw_body, body_read_callback, offline, chunked, content_length_header_value)
    assert result == b"request body"


def test_get_multipart_data_and_content_type():
    data = uploads.MultipartRequestDataDict()
    data.add_field('field1', 'value1')
    data.add_field('field2', 'value2')

    result = uploads.get_multipart_data_and_content_type(data)
    assert isinstance(result[0], uploads.MultipartEncoder)
    assert isinstance(result[1], str)


def test_compress_request_with_economical_data():
    request = uploads.requests.PreparedRequest()
    request.body = b"request body"
    always = False

    uploads.compress_request(request, always)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in request.headers


def test_compress_request_with_non_economical_data():
    request = uploads.requests.PreparedRequest()
    request.body = b"request body" * 100
    always = False

    uploads.compress_request(request, always)
    assert 'Content-Encoding' not in request.headers


def test_compress_request_with_always_true():
    request = uploads.requests.PreparedRequest()
    request.body = b"request body" * 100
    always = True

    uploads.compress_request(request, always)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in request.headers
