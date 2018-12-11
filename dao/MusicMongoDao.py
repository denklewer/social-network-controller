from pymongo import MongoClient
import config
import logging
from dao.MusicDao import MusicDao

class MusicMongoDao(MusicDao):
    logger = logging.getLogger("MusicDao")
    client = MongoClient(config.MONGODB_URL % ("denis", "Ze97gCD6WUQF"))
    database = client["tu-graz"]
    collection = database["Music"]
    publicProjection={"_id": 1.0,
                        "name": 1.0,
                        "singer": 1.0,
                        "album": 1.0,
                       "rating": 1.0,
                       "size": 1.0,
                       "owner": 1.0}

    def load_music(self, user):
        query = {}
        query['owner'] = user
        song_list = []
        try:
            result = self.collection.find(query, projection=self.publicProjection)

            for doc in result:
                song_list.append(doc)
            song_list = {"Song": [i for i in song_list]}
        except Exception as e:
            self.logger.exception(str(e))
        return song_list
