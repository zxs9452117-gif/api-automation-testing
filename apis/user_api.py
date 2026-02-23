from .base_api import BaseApi

class UserApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.USERS_PATH = "/users"

    def get_user_list(self):
        """獲取用戶列表"""
        return self.get(self.USERS_PATH)

    def create_user(self, name, email):
        """創建新用戶"""
        payload = {
            "name": name,
            "email": email
        }
        return self.post(self.USERS_PATH, json=payload)

    def get_single_user(self, user_id):
        """
        獲取特定單一用戶資料
        """
        return self.get(f"{self.USERS_PATH}/{user_id}")