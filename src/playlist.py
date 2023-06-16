from datetime import timedelta

import isodate
from googleapiclient.discovery import build
from src.channel import api_key

from src.video import PLVideo, Video


class MixVideo:
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist

    def get_video(self):
        video = self.youtube.playlistItems().list(playlistId=self.id_playlist,
                                                  part='contentDetails',
                                                  maxResults=50,
                                                  ).execute()
        return video

    def get_video_id(self):
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in
                                self.get_video()['items']]
        return video_ids


class PlayList(MixVideo, Video):

    def __init__(self, id_playlist):
        super().__init__(id_playlist)
        self.data = self.get_data(id_playlist)
        self.title = self.data['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={id_playlist}'

    def __str__(self):

        return f"{self.total_duration.str('%H:%M:%S')}"

    def get_data(self, playlist):
        """ Получает данные от YouTube. """

        self.data = MixVideo.youtube.playlists().list(part='snippet',
                                                      id=playlist).execute()
        return self.data

    def show_best_video(self):
        lst_video = []
        for video in self.get_video_id():
            v = Video(video)
            lst_video.append(v)

        return f'https://youtube/{max(lst_video).id_video}'

    @property
    def total_duration(self):

        video_response = self.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(self.get_video_id())
        ).execute()
        total_time = timedelta()

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_time += duration
        return total_time
