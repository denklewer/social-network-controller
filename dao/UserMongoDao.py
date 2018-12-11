# Requires pymongo 3.6.0+
from pymongo import MongoClient
import config
import logging
from bson.objectid import ObjectId
from dao.UserDao import UserDao


class UserMongoDao(UserDao):
    logger = logging.getLogger("userDao")
    client = MongoClient(config.MONGODB_URL % ("denis", "Ze97gCD6WUQF"))
    database = client["tu-graz"]
    collection = database["User"]

    publicProjection = {"_id": 1.0,
                        "name": 1.0,
                        "lastname": 1.0,
                        "small_link": 1.0,
                        "slogan": 1.0,
                        "company": 1.0,
                        "username": 1.0,
                        "email": 1.0,
                        "city": 1.0,
                        "country": 1.0,
                        "postal_code": 1.0,
                        "address": 1.0,
                        "description": 1.0}

    privateProjection = {"email": 1.0, "password": 1.0}

    def get_users(self):
        query = {}
        cursor = self.collection.find(query, projection=self.publicProjection)
        user_list = []
        try:
            for doc in cursor:
                user_list.append(doc)
        except Exception as e:
            self.logger.exception(str(e))
        return user_list

    def get_user_by_id(self, id):
        query = {}
        query["_id"] = ObjectId(id)
        result = ""
        try:
            result = self.collection.find_one(query, projection=self.publicProjection)
            print(result.get('_id'));
        except Exception as e:
            self.logger.exception(str(e))
        return result

    def insert_user(self, user):
        user_id = ""
        try:
            user_id = self.collection.insert_one(user).inserted_id
        except Exception as e:
            self.logger.exception(str(e))
        return user_id

    def update_user_by_email(self, user):
        query = {"email": user.get('email')}
        self.validate_public(user)
        new_values = {"$set": user}

        modified_count = 0
        try:
            modified_count = self.collection.update_one(query, new_values).modified_count
        except Exception as e:
            self.logger.exception(str(e))
        return modified_count

    def login(self, email, password):
        query = {}
        query["email"] = email
        result = ""
        try:
            result = self.collection.find_one(query, projection=self.privateProjection)

            if (result.get('password') == password):
                result = self.collection.find_one(query, projection=self.publicProjection)
            else:
                result = {}
        except Exception as e:
            self.logger.exception(str(e))
        return result

    def get_user_private(self, email):
        query = {}
        query["email"] = email
        result = {}
        try:
            result = self.collection.find_one(query, projection=self.privateProjection)
        except Exception as e:
            self.logger.exception(str(e))
        return result

    def get_user_public(self, email):
        query = {}
        query["email"] = email
        result = {}
        try:
            result = self.collection.find_one(query, projection=self.publicProjection)
        except Exception as e:
            self.logger.exception(str(e))
        return result


    def update_user_password(self, user, password):
        query = {"_id": user.get('_id')}
        password_dict = {"password": password}
        new_values = {"$set": password_dict}
        modified_count = 0
        try:
            modified_count = self.collection.update_one(query, new_values).modified_count
        except Exception as e:
            self.logger.exception(str(e))
        return modified_count

    def update_user_login(self, user, login):
        query = {"_id": user.get('_id')}
        login_dict = {"login": login}
        new_values = {"$set": login_dict}
        modified_count = 0
        try:
            modified_count = self.collection.update_one(query, new_values).modified_count
        except Exception as e:
            self.logger.exception(str(e))
        return modified_count

    def get_team(self, user):
        query = {}
        query["email"] = user
        result = {}
        user_list=[]
        try:
            result = self.collection.find_one(query, projection=self.publicProjection)
            query1={"company": result.get('company')}
            resultout={}
            resultout=self.collection.find(query1, projection=self.publicProjection)

            for doc in resultout:
                user_list.append(doc)
            user_list1 = {"title":[i for i in user_list]}
        except Exception as e:
            self.logger.exception(str(e))
        return user_list1

    @staticmethod
    def validate_public(user):
        try:
            del user["password"]
            del user["login"]
        except KeyError:
            pass

    def close(self):
        self.client.close()
