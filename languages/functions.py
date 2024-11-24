import npyscreen

def menu_languages(self):
    self.parentApp.switchForm("LANGUAGES")

def load_buttons_from_config(self, config_path):
    """
    Загружает список кнопок из JSON-файла.
    """
    with open(config_path, "r") as file:
        return json.load(file)

def language_cancel(self):
    self.parentApp.switchForm("MAIN")