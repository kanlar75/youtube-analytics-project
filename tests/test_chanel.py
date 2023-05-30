import contextlib
import io

from src.channel import Channel


def test_init(obj_chanel):
    assert isinstance(obj_chanel, Channel)
    obj1 = Channel("test")
    assert obj1.channel_id == "test"


def test_print_info(obj_chanel, test_data):
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        obj_chanel.print_info()
    assert s.getvalue() == f'{test_data}'
