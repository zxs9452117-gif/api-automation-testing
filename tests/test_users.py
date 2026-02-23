import pytest
from utils.data_loader import load_json_data
from utils.validator import validate_json_schema

test_data = load_json_data("user_data.json")

class TestUserManagement:

    def test_get_user_list_successfully(self, user_api):
        """測試獲獲取用戶列表並驗證結構"""
        response = user_api.get_user_list()

        assert response.status_code == 200
        res_json = response.json()

        validate_json_schema(res_json, "user_schema.json")

        assert len(res_json) > 0
        print(f"\n成功取得並驗證 {len(res_json)} 筆使用者資料結構！")

    def test_create_user_successfully(self, user_api):
        """測試創建用戶 (結合 JSON 資料驅動)"""
        payload = test_data["valid_new_user"]

        response = user_api.create_user(payload["name"], payload["email"])

        assert response.status_code == 201
        res_json = response.json()

        assert res_json["name"] == payload["name"]
        assert res_json["email"] == payload["email"]
        assert "id" in res_json
        print(f"\n成功創建用戶: {res_json['name']} (ID: {res_json['id']})")