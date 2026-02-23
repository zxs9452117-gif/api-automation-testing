import pytest
from utils.data_loader import load_json_data

test_data = load_json_data("user_data.json")
class TestUserManagement:


    def test_get_user_list_successfully(self, user_api):
        """測試獲取用戶列表"""
        response = user_api.get_user_list()

        assert response.status_code == 200

        res_json = response.json()
        assert isinstance(res_json, list)
        assert len(res_json) > 0

        assert "email" in res_json[0]
        print(f"\n成功取得 {len(res_json)} 筆使用者資料！")

    def test_create_user_successfully(self, user_api):
        """測試創建用戶 (結合 JSON 資料驅動)"""

        payload = test_data["valid_new_user"]

        response = user_api.create_user(payload["name"], payload["email"])

        assert response.status_code == 201
        res_json = response.json()

        assert res_json["name"] == payload["name"]
        assert res_json["email"] == payload["email"]
        assert "id" in res_json