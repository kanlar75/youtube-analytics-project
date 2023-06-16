import json
import os

from googleapiclient.discovery import build

# Получаем ключ API из переменной среды
api_key = os.getenv('YOU_TUBE_API_KEY')


class Channel:
    """ Класс для ютуб-канала. """

    # объект для работы с API
    youtube = None
    data = None

    def __init__(self, id_str: str) -> None:
        """ Экземпляр инициализируется по id канала. """

        self.data = self.get_data(id_str)
        self._channel_id = id_str
        self.title = self.data['items'][0]['snippet']['title']
        self.description = \
            self.data['items'][0]['snippet']['description'].split('\n')[0]
        self.url = f"https://www.youtube.com/channel/" \
                   f"{self.data['items'][0]['id']}"
        self.subscriber = int(self.data['items'][0]['statistics'][
                                  'subscriberCount'])
        self.video_count = int(self.data['items'][0]['statistics'][
                                   'videoCount'])
        self.count_viewers = int(self.data['items'][0]['statistics'][
                                     'viewCount'])

    def __str__(self):
        """ Строковое представление экземпляра: наименование канала и url"""

        return f'{self.title} ({self.url})'

    def __eq__(self, other):
        """ Возвращает True или False (равенство числа подписчиков) """

        if self.validate(other):
            return self.subscriber == other.subscriber

    def __add__(self, other):
        """ Возвращает сумму числа подписчиков двух экземпляров """

        if self.validate(other):
            return self.subscriber + other.subscriber

    def __sub__(self, other):
        """ Возвращает разность числа подписчиков двух экземпляров """

        if self.validate(other):
            return self.subscriber - other.subscriber

    def __lt__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """

        if self.validate(other):
            return self.subscriber < other.subscriber

    def __le__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """

        if self.validate(other):
            return self.subscriber <= other.subscriber

    def __gt__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """

        if self.validate(other):
            return self.subscriber > other.subscriber

    def __ge__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """

        if self.validate(other):
            return self.subscriber >= other.subscriber

    @classmethod
    def get_data(cls, id_str):
        """ Получает данные от YouTube. """

        cls.youtube = cls.get_service()
        cls.data = cls.youtube.channels().list(id=id_str, part='snippet, ' \
                                                               'statistics').execute()
        return cls.data

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с YouTube API. """

        cls.youtube = build('youtube', 'v3', developerKey=api_key)
        return cls.youtube

    @classmethod
    def validate(cls, obj):
        """ Проверяет принадлежность объекта к классу Channel. """

        if not isinstance(obj, Channel):
            raise TypeError('Операнд справа должен быть экземпляром класса '
                            'Channel!')
        return True

    @property
    def channel_id(self):
        """ Возвращаем id канала. """

        return self._channel_id

    # @channel_id.setter
    # def channel_id(self, value):
    #     if isinstance(value, str):
    #         self._channel_id = value

    def to_json(self, file_name='moscowpython.json'):
        """ Запись атрибутов в файл 'moscowpython.json'. """

        script_path = os.path.abspath(__file__)
        path_list = script_path.split(os.sep)
        script_directory = path_list[0:len(path_list) - 1]
        rel_path = f"/{file_name}"
        path = "/".join(script_directory) + "/" + rel_path
        with open(path, 'w') as f:
            json.dump(self.__dict__, f, indent=4, ensure_ascii=False)

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале в json-подобном удобном
        формате с отступами.
        """

        data = self.get_service().channels().list(id=self.channel_id,
                                                  part='snippet,statistics').execute()
        print(json.dumps(data, indent=2, ensure_ascii=False))
