import json
import os

from googleapiclient.discovery import build

# Получаем ключ API из переменной среды
api_key = os.getenv('YOU_TUBE_API_KEY')


class Channel:
    """ Класс для ютуб-канала. """

    # объект для работы с API
    youtube = None

    def __init__(self, id_str: str) -> None:
        """ Экземпляр инициализируется по id канала. """
        data = Channel.get_service().channels().list(id=id_str,
                                                     part='snippet,'
                                                          'statistics').execute()
        self._channel_id = id_str
        self.title = data['items'][0]['snippet']['title']
        self.description = \
            data['items'][0]['snippet']['description'].split('\n')[0]
        self.url = f"https://www.youtube.com/channel/" \
                   f"{data['items'][0]['id']}"
        self.subscriber = int(data['items'][0]['statistics'][
                                  'subscriberCount'])
        self.video_count = int(data['items'][0]['statistics']['videoCount'])
        self.count_viewers = int(data['items'][0]['statistics']['viewCount'])

    def __str__(self):
        """ Строковое представление экземпляра: наименование канала и url"""

        return f'{self.title} ({self.url})'

    def __eq__(self, other):
        """ Возвращает True или False (равенство числа подписчиков) """

        obj = self.is_belongs_to_class(other)
        return self.subscriber == obj

    def __add__(self, other):
        """ Возвращает сумму числа подписчиков двух экземпляров """

        obj = self.is_belongs_to_class(other)
        return self.subscriber + obj

    def __sub__(self, other):
        """ Возвращает разность числа подписчиков двух экземпляров """

        obj = self.is_belongs_to_class(other)
        return self.subscriber - obj

    def __lt__(self, other):
        """ Возвращает True или False """

        obj = self.is_belongs_to_class(other)
        return self.subscriber < obj

    def __le__(self, other):
        """ Возвращает True или False """

        obj = self.is_belongs_to_class(other)
        return self.subscriber <= obj

    def __gt__(self, other):
        """ Возвращает True или False """

        obj = self.is_belongs_to_class(other)
        return self.subscriber > obj

    def __ge__(self, other):
        """ Возвращает True или False """

        obj = self.is_belongs_to_class(other)
        return self.subscriber >= obj

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с YouTube API. """

        cls.youtube = build('youtube', 'v3', developerKey=api_key)
        return cls.youtube

    @classmethod
    def is_belongs_to_class(cls, obj):
        if not isinstance(obj, Channel):
            raise TypeError('Операнд справа должен быть экземпляром класса '
                            'Channel!')
        return obj.subscriber

    # возвращаем id канала
    @property
    def channel_id(self):
        return self._channel_id

    # @channel_id.setter
    # def channel_id(self, value):
    #     if isinstance(value, str):
    #         self._channel_id = value

    def to_json(self, file_name='moscowpython.json'):
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

        data = Channel.get_service().channels().list(id=self.channel_id,
                                                     part='snippet,statistics').execute()
        print(json.dumps(data, indent=2, ensure_ascii=False))
