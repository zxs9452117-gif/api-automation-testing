import pytest
from apis.user_api import UserApi
from apis.product_api import ProductApi

@pytest.fixture(scope="session")
def user_api():
    """
    初始化 UserApi 對象，並共享給所有的測試案例。
    scope="session" 代表整個測試過程只會實例化一次，節省資源。
    """
    return UserApi()

@pytest.fixture(scope="session")
def product_api():
    """
    初始化 ProductApi 對象，並共享給所有的測試案例。
    """
    return ProductApi()