import configparser
import os

def get_config(section, key):
    config = configparser.ConfigParser()

    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, 'config.ini')

    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到設定檔！Python 正在這裡尋找檔案，請確認路徑是否正確: {path}")

    config.read(path)
    return config.get(section, key)