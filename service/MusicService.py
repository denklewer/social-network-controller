from dao.MusicDao import MusicDao
from dao.MusicMongoDao import MusicMongoDao


class MusicService:
    music_dao = MusicDao()

    def setup_music_dao(self):
        self.music_dao = MusicMongoDao();

    def insert_music(self, music):
        return self.music_dao.insert_music(music)
