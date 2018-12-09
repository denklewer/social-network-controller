from pymongo import MongoClient
import config
import logging
from bson.objectid import ObjectId
from dao.MusicDao import MusicDao
import gridfs
# For MIME types
import magic


class MusicMongoDao(MusicDao):
    logger = logging.getLogger("userDao")
    client = MongoClient(config.MONGODB_URL % ("denis", "Ze97gCD6WUQF"))
    database = client["tu-graz"]
    collection = database["Music"]
    fs = gridfs.GridFS(database)


def insert_music(self, music):
    music_id = ""
    try:
        mime = magic.Magic(mime=True)
        mime.from_file(music['file'])
        file_id = self.fs.put(open(music['file']), content_type=mime, filename=music["name"])
        music['data'] = file_id
        music_id = self.collection.insert_one(music).inserted_id
    except Exception as e:
        self.logger.exception(str(e))
    return music_id
