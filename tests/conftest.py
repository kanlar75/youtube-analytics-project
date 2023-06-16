import json

import pytest

from src.channel import Channel
from src.playlist import PlayList
from src.video import Video, PLVideo


@pytest.fixture
def test_obj1():
    """ Тестовый объект channel moscowpython"""

    test_obj1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    return test_obj1


@pytest.fixture
def test_obj2():
    """ Тестовый объект channel highload """

    test_obj2 = Channel('UCwHL6WHUarjGfUM_586me8w')
    return test_obj2


@pytest.fixture
def test_obj3():
    """ Тестовый объект класса Vidio """

    test_obj3 = Video('AWX4JnAnjBE')
    return test_obj3


@pytest.fixture
def test_obj4():
    """ Тестовый объект класса PLVideo """

    test_obj4 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    return test_obj4


@pytest.fixture
def test_obj5():
    """ Тестовый объект Playlist """

    test_obj5 = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    return test_obj5


@pytest.fixture
def test_obj1_sub():
    """ channel moscowpython, число подписчиков. """

    test_obj1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    return test_obj1.subscriber


@pytest.fixture
def test_obj2_sub():
    """ channel highload, число подписчиков. """

    test_obj2 = Channel('UCwHL6WHUarjGfUM_586me8w')
    return test_obj2.subscriber


@pytest.fixture
def test_data(test_obj1):
    data = Channel.get_service().channels().list(id=test_obj1.channel_id,
                                                 part='snippet,statistics').execute()
    response = json.dumps(data, indent=2, ensure_ascii=False)
    return response


@pytest.fixture(scope='module')
def json_data():
    """ Тестовые данные. """

    data = {
        "_channel_id": "UC-OVMPlMA3-YCIeg4z5z23A",
        "title": "MoscowPython",
        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)",
        "url": "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A",
        "subscriber": "26000",
        "video_count": "687",
        "count_viewers": "2319191"
    }
    return data


@pytest.fixture(scope='module')
def temp_file_json(tmpdir_factory, json_data):
    """
    Записываем тестовые данные в файл 'test.json' во временной
    директории.
    """
    temp_data = json_data
    file = tmpdir_factory.mktemp('data').join('test.json')

    with file.open('w') as f:
        json.dump(temp_data, f)
    return file
