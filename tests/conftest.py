import pytest

from src.channel import Channel


@pytest.fixture
def obj_chanel():
    test = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    return test


@pytest.fixture
def test_data():
    response = ('{\n'
                '  "kind": "youtube#channelListResponse",\n'
                '  "etag": "kPl2SkUvAWW34VR8CY2rnWxZtZk",\n'
                '  "pageInfo": {\n'
                '    "totalResults": 1,\n'
                '    "resultsPerPage": 5\n'
                '  },\n'
                '  "items": [\n'
                '    {\n'
                '      "kind": "youtube#channel",\n'
                '      "etag": "mAJkqj7ThYQVf5SAQ0s5EuPg4Rg",\n'
                '      "id": "UC-OVMPlMA3-YCIeg4z5z23A",\n'
                '      "snippet": {\n'
                '        "title": "MoscowPython",\n'
                '        "description": "Видеозаписи со встреч питонистов и джангистов в '
                'Москве и не только. :)\\nПрисоединяйтесь: '
                'https://www.facebook.com/groups/MoscowDjango! :)",\n'
                '        "customUrl": "@moscowdjangoru",\n'
                '        "publishedAt": "2012-07-13T09:48:44Z",\n'
                '        "thumbnails": {\n'
                '          "default": {\n'
                '            "url": '
                '"https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj",\n'
                '            "width": 88,\n'
                '            "height": 88\n'
                '          },\n'
                '          "medium": {\n'
                '            "url": '
                '"https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj",\n'
                '            "width": 240,\n'
                '            "height": 240\n'
                '          },\n'
                '          "high": {\n'
                '            "url": '
                '"https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj",\n'
                '            "width": 800,\n'
                '            "height": 800\n'
                '          }\n'
                '        },\n'
                '        "localized": {\n'
                '          "title": "MoscowPython",\n'
                '          "description": "Видеозаписи со встреч питонистов и джангистов в '
                'Москве и не только. :)\\nПрисоединяйтесь: '
                'https://www.facebook.com/groups/MoscowDjango! :)"\n'
                '        },\n'
                '        "country": "RU"\n'
                '      },\n'
                '      "statistics": {\n'
                '        "viewCount": "2315392",\n'
                '        "subscriberCount": "26000",\n'
                '        "hiddenSubscriberCount": false,\n'
                '        "videoCount": "686"\n'
                '      }\n'
                '    }\n'
                '  ]\n'
                '}\n')

    return response
