import json

def load_buttons_from_config(config_path):
    """
    Загружает список кнопок из JSON-файла.
    """
    with open(config_path, "r") as file:
        return json.load(file)