import npyscreen
import json
from languages.functions import language_cancel

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm)


class MainForm(npyscreen.Form):
    def create(self):
        # Создаем меню
        self.menu = self.add(
            npyscreen.BoxTitle,
            name="Arch Install",
            max_height=15,
            max_width=30,
            relx=1,
            rely=1,
        )

        # Создаем дополнительное меню
        self.menu2 = self.add(
            npyscreen.BoxTitle,
            name="Additional Options",
            max_height=15,
            max_width=50,
            relx=33,
            rely=1,
        )

        # Загружаем кнопки из конфигурации
        self.menu2_buttons = self.load_buttons_from_config("./languages/languages_config.json")
        # Добавляем кнопки в меню
        self.add_buttons_to_menu()

        # Привязываем обработчик выбора
        self.menu2.when_value_edited = self.handle_menu2_selection

    def load_buttons_from_config(self, config_path):
        """
        Загружает список кнопок из JSON-файла.
        """
        with open(config_path, "r") as file:
            return json.load(file)

    def add_buttons_to_menu(self):
        """
        Добавляет кнопки из конфигурации в меню.
        """
        for button in self.menu2_buttons:
            self.menu2.values.append(button["name"])

    def handle_menu2_selection(self):
        """
        Обрабатывает выбор в меню 2 и выполняет соответствующее действие.
        """
        selected_index = self.menu2.value
        if selected_index is not None:
            selected_button = self.menu2_buttons[selected_index]
            action_name = selected_button["action"]

            # Выполняем действие в зависимости от action
            if action_name == "language_cancel":
                language_cancel(self)  # Передаем текущую форму в функцию
            elif hasattr(self, action_name):
                action_method = getattr(self, action_name)
                action_method()
            else:
                npyscreen.notify_confirm(f"Action '{action_name}' is not implemented!")

    def language_action_english(self):
        """
        Метод для кнопки "English".
        """
        npyscreen.notify_confirm("English selected!")

    def language_action_russian(self):
        """
        Метод для кнопки "Russian".
        """
        npyscreen.notify_confirm("Russian selected!")

    def language_action_placeholder(self):
        """
        Метод-заглушка для дополнительных кнопок.
        """
        npyscreen.notify_confirm("This action is not implemented yet.")


if __name__ == "__main__":
    app = MyApp()
    app.run()
