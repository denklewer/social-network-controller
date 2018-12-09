
from dao.UserMongoDao import UserMongoDao


class UserService:
    dao = UserMongoDao()

    def login(self, email, password):
        result = self.dao.get_user_private(email)
        if result is not None and result.get('password') == password:
            result = self.dao.get_user_public(email)
        else:
            result = {}
        return result

    def get_user(self, email):
        result = self.dao.get_user_public(email)
        if result is None:
            result = {}
        return result

    def update_user(self, user):
        result = self.dao.update_user_by_email(user)
        if result is None:
            result = {}
        return result

    def insert_user(self, user):
        result = self.dao.insert_user(user)
        if result is None:
            result = {}
        return result





