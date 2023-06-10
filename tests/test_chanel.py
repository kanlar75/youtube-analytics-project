import contextlib
import io
import json

import pytest

from src.channel import Channel


# Тестируем инициализацию
def test_init(test_obj1):
    assert isinstance(test_obj1, Channel)
    obj1 = Channel("UC-OVMPlMA3-YCIeg4z5z23A")
    assert obj1.channel_id == "UC-OVMPlMA3-YCIeg4z5z23A"


# Тестируем print
def test_print_info(test_obj1, test_data):
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        test_obj1.print_info()
        assert s.getvalue() == f"{test_data}\n"


# Тест записи в файл
def test_to_json(test_obj1, temp_file_json):
    test_obj1.to_json()

    with open(temp_file_json, 'r') as f:
        assert test_obj1.title == json.load(f)['title']


# Тест __str__
def test_str(test_obj1):
    assert test_obj1.__str__() == 'MoscowPython (' \
                                  'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'


# Тест магических методов. """
def test_magic(test_obj1, test_obj2, test_obj1_sub, test_obj2_sub):
    assert (test_obj1 < test_obj2) is True
    assert (test_obj1 <= test_obj2) is True
    assert (test_obj1 > test_obj2) is False
    assert (test_obj1 >= test_obj2) is False
    assert (test_obj1 == test_obj2) is False
    assert test_obj1 + test_obj2 == test_obj1_sub + test_obj2_sub
    assert test_obj1 - test_obj2 == test_obj1_sub - test_obj2_sub


# Тест Raise в методе класса, передаем строку и число
def test_validate(test_obj1):
    with pytest.raises(TypeError):
        test_obj1.validate("test")
        test_obj1.validate(1)
