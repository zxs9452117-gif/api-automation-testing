from utils.validator import validate_json_schema

class TestProductCRUD:

    def test_create_and_verify_product(self, product_api):
        """
        測試場景：新增貼文並驗證回傳內容 (Create)
        """
        title = "自動化測試專案"
        body = "這是一篇由 Pytest 自動產生的測試貼文內容"

        response = product_api.create_product(title, body)

        assert response.status_code == 201
        res_data = response.json()
        assert res_data["title"] == title
        assert res_data["body"] == body
        assert "id" in res_data
        print(f"\n[Create] 成功建立產品 ID: {res_data['id']}")

    def test_get_product_details(self, product_api):
        """
        測試場景：獲取單一貼文詳情 (Read)
        """
        product_id = 1
        response = product_api.get_product_details(product_id)

        assert response.status_code == 200
        res_data = response.json()
        validate_json_schema(res_data, "product_schema.json")
        assert res_data["id"] == product_id
        print(f"\n[Read] 成功獲取並驗證產品 ID {product_id} 的結構與內容")

    def test_update_product_completely(self, product_api):
        """
        測試場景：修改現有貼文內容 (Update)
        """
        product_id = 1
        new_title = "修改後的標題"
        new_body = "修改後的內容"

        response = product_api.update_product_info(product_id, new_title, new_body)

        assert response.status_code == 200
        res_data = response.json()
        assert res_data["title"] == new_title
        assert res_data["body"] == new_body
        print(f"\n[Update] 產品 ID {product_id} 已成功更新")

    def test_delete_product_successfully(self, product_api):
        """
        測試場景：刪除貼文 (Delete)
        """
        product_id = 1
        response = product_api.delete_product(product_id)

        assert response.status_code in [200, 204]
        print(f"\n[Delete] 產品 ID {product_id} 已成功刪除")

    def test_product_lifecycle_flow(self, product_api):
        """
        整合測試：新增 -> 修改 -> 刪除
        注意：因 JSONPlaceholder 不會真的儲存 POST 的資料，
        後續的 Update 與 Delete 需使用伺服器既有的 ID (如 ID 1) 進行模擬。
        """
        res_create = product_api.create_product("Flow Test", "Content")
        assert res_create.status_code == 201
        print(f"\n[Flow] 新增功能驗證成功，模擬生成的 ID 為: {res_create.json()['id']}")

        existing_id = 1
        res_update = product_api.update_product_info(existing_id, "Updated Flow", "New Content")
        assert res_update.status_code == 200
        assert res_update.json()["title"] == "Updated Flow"
        print(f"\n[Flow] 修改功能驗證成功 (針對 ID {existing_id})")

        res_delete = product_api.delete_product(existing_id)
        assert res_delete.status_code == 200
        print(f"\n[Flow] 刪除功能驗證成功 (針對 ID {existing_id})")