from jsonschema import validate
from utils.data_loader import load_json_data

def validate_json_schema(instance, schema_file):
    """
    驗證 JSON 回傳內容是否符合指定的 Schema 定義
    """
    schema = load_json_data(schema_file)
    validate(instance=instance, schema=schema)