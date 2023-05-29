import json
import os

from googleapiclient.discovery import build

# Получаем ключ API из переменной среды
api_key = os.getenv('YOU_TUBE_API_KEY')

# создаем специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """ Класс для ютуб-канала. """

    def __init__(self, channel_id: str) -> None:
        """ Экземпляр инициализируется по id канала. """
        self.channel_id = channel_id

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале в json-подобном удобном
        формате с отступами.
        """

        data = youtube.channels().list(id=self.channel_id,
                                          part='snippet,statistics').execute()
        print(json.dumps(data, indent=2, ensure_ascii=False))




