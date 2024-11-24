import npyscreen
import json
from languages.functions import language_cancel
from functions.load_from_config import load_buttons_from_config
from functions.add_buttons_to_menu import add_buttons_to_menu

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm)
        self.addForm('LANGUAGES', LanguageForm)

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

        self.menu_buttons = self.load_buttons_from_config("./main_menu/mainmenu.json")
        self.add_buttons_to_menu()

    #     # Загружаем кнопки из конфигурации
    #     self.menu2_buttons = self.load_buttons_from_config("./languages/languages_config.json")
    #     # Добавляем кнопки в меню
    #     self.add_buttons_to_menu()

    #     # Привязываем обработчик выбора
    #     self.menu2.when_value_edited = self.handle_menu2_selection

    # def handle_menu2_selection(self):
    #     """
    #     Обрабатывает выбор в меню 2 и выполняет соответствующее действие.
    #     """
    #     selected_index = self.menu2.value
    #     if selected_index is not None:
    #         selected_button = self.menu2_buttons[selected_index]
    #         action_name = selected_button["action"]

    #         # Выполняем действие в зависимости от action
    #         if action_name == "language_cancel":
    #             language_cancel(self)  # Передаем текущую форму в функцию
    #         elif hasattr(self, action_name):
    #             action_method = getattr(self, action_name)
    #             action_method()
    #         else:
    #             npyscreen.notify_confirm(f"Action '{action_name}' is not implemented!")

    # def language_action_english(self):
    #     """
    #     Метод для кнопки "English".
    #     """
    #     npyscreen.notify_confirm("English selected!")

    # def language_action_russian(self):
    #     """
    #     Метод для кнопки "Russian".
    #     """
    #     npyscreen.notify_confirm("Russian selected!")

    # def language_action_placeholder(self):
    #     """
    #     Метод-заглушка для дополнительных кнопок.
    #     """
    #     npyscreen.notify_confirm("This action is not implemented yet.")

class LanguageForm(npyscreen.Form):
    def create(self):
        self.menu2 = self.add(
            npyscreen.BoxTitle,
            name="Additional Options",
            max_height=15,
            max_width=50,
            relx=33,
            rely=1,
        )

        self.menu = self.add(
            npyscreen.BoxTitle,
            name="Arch Install",
            max_height=15,
            max_width=30,
            relx=1,
            rely=1,
        )

        self.menu2_buttons = self.load_buttons_from_config("./languages/languages_config.json")


if __name__ == "__main__":
    app = MyApp()
    app.run()
