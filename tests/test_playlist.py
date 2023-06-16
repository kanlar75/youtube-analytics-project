import datetime


def test_init(test_obj5):
    assert test_obj5.title == "Moscow Python Meetup №81"
    assert test_obj5.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj" \
                    "-n2qLkEM2Hj96LO6uqgQw"


def test_total_duration(test_obj5):
    duration = test_obj5.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(test_obj5.total_duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0


def test_show_best_video(test_obj5):
    assert test_obj5.show_best_video() == "https://youtube/cUGyMzWQcGM"
