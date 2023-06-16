import pytest

from src.video import Video, PLVideo


# Тестируем инициализацию класса Video
def test_init_video(test_obj3):
    assert isinstance(test_obj3, Video)
    obj3 = Video('AWX4JnAnjBE')
    assert obj3.id_video == "AWX4JnAnjBE"


# Тестируем инициализацию класса PLVideo
def test_init_plv(test_obj4):
    assert isinstance(test_obj4, PLVideo)
    assert test_obj4.id_video == "4fObz_qw9u4"
    assert test_obj4.id_playlist == "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC"


def test_str(test_obj3):
    assert test_obj3.__str__() == 'GIL в Python: зачем он нужен и как с этим жить'


# Тест Raise в методе класса validate, передаем строку и число
def test_validate(test_obj3):
    with pytest.raises(TypeError):
        test_obj3.validate("test")
        test_obj3.validate(1)
