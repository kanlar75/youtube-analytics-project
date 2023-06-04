import json

import pytest

from src.channel import Channel


@pytest.fixture
def obj_chanel():
    test_obj = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    return test_obj


@pytest.fixture
def test_data(obj_chanel):

    data = Channel.get_service().channels().list(id=obj_chanel.channel_id,
                                                 part='snippet,statistics').execute()
    response = json.dumps(data, indent=2, ensure_ascii=False)
    return response


@pytest.fixture(scope='module')
def json_data():
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
