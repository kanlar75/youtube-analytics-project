import contextlib
import io
import json

from src.channel import Channel


def test_init(obj_chanel):
    assert isinstance(obj_chanel, Channel)
    obj1 = Channel("UC-OVMPlMA3-YCIeg4z5z23A")
    assert obj1.channel_id == "UC-OVMPlMA3-YCIeg4z5z23A"


def test_print_info(obj_chanel, test_data):
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        obj_chanel.print_info()
    assert s.getvalue() == f"{test_data}\n"


def test_to_json(obj_chanel, temp_file_json):
    obj_chanel.to_json()

    with open(temp_file_json, 'r') as f:
        assert obj_chanel.title == json.load(f)['title']
