from googleapiclient.discovery import build

from src.channel import api_key


class Video:
    """ Класс для видео ютуб-канала. """

    data = None
    youtube = None

    def __init__(self, id_str):
        self.data = self.get_data(id_str)

        self.id_video = id_str
        self.title = self.data['items'][0]['snippet']['title']
        self.viewers = self.data['items'][0]['statistics']['viewCount']
        self.likes = self.data['items'][0]['statistics']['likeCount']
        self.url = f'https://www.youtube.com/watch?v={self.id_video}'

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с YouTube API. """

        cls.youtube = build('youtube', 'v3', developerKey=api_key)
        return cls.youtube

    @classmethod
    def get_data(cls, id_str):
        """ Получает данные от YouTube. """

        cls.youtube = cls.get_service()
        cls.data = cls.youtube.videos().list(id=id_str, part='snippet, ' \
                                                             'statistics').execute()
        return cls.data

    def __str__(self):
        """ Строковое представление экземпляра: наименование канала. """

        return f'{self.title}'


class PLVideo(Video):
    """ Класс для видео и плейлистов ютуб-канала. """

    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
