
from dao.MusicMongoDao import MusicMongoDao


class MusicService:
    music_dao = MusicMongoDao()

    def setup_music_dao(self):
        self.music_dao = MusicMongoDao();

    def insert_music(self, music):
        return self.music_dao.insert_music(music)

    def load_music(self, user):
        result = self.music_dao.load_music(user)
        if result is None:
            result=[]
        return result

