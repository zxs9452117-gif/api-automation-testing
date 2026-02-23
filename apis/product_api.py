from .base_api import BaseApi

class ProductApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.RESOURCE_PATH = "/posts"

    def get_all_products(self):
        """
        獲取所有產品列表 (GET)
        """
        return self.get(self.RESOURCE_PATH)

    def get_product_details(self, product_id):
        """
        獲取單一產品詳情 (GET)
        """
        return self.get(f"{self.RESOURCE_PATH}/{product_id}")

    def create_product(self, title, body, user_id=1):
        """
        新增產品 (POST)
        """
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self.post(self.RESOURCE_PATH, json=payload)

    def update_product_info(self, product_id, title, body):
        """
        修改產品資訊 (PUT)
        """
        payload = {
            "id": product_id,
            "title": title,
            "body": body
        }
        return self.put(f"{self.RESOURCE_PATH}/{product_id}", json=payload)

    def delete_product(self, product_id):
        """
        刪除產品 (DELETE)
        """
        return self.delete(f"{self.RESOURCE_PATH}/{product_id}")