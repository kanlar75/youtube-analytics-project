import datetime


# Тестируем инициализацию класса PlayList

def test_init(test_obj5):
    assert test_obj5.title == "Moscow Python Meetup №81"
    assert test_obj5.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj" \
                            "-n2qLkEM2Hj96LO6uqgQw"


# Тестируем принадлежность к классу `datetime.timedelta`, суммарную
# длительность плейлиста, строковое представление длительности
def test_total_duration(test_obj5):
    duration = test_obj5.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(test_obj5.total_duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0


# Тестируем возвращение строки на самое популярное видео из плейлиста (по
# количеству лайков)
def test_show_best_video(test_obj5):
    assert test_obj5.show_best_video() == "https://youtube/cUGyMzWQcGM"
