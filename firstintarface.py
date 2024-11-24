import npyscreen
import json
from languages.functions import language_cancel
from functions.load_from_config import load_buttons_from_config
from functions.add_buttons_to_menu import add_buttons_to_menu
from languages.functions import menu_languages


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

        self.menu_buttons = load_buttons_from_config("./main_menu/mainmenu.json")
        add_buttons_to_menu(self.menu, self.menu_buttons)

        self.menu.when_value_edited = self.handle_menu_selection

    def handle_menu_selection(self):
        """
        Обрабатывает выбор кнопки в меню.
        """
        action = self.menu_buttons[self.menu.value].get("action")  # Получаем действие

        match action:
            case "menu_languages":
                self.parentApp.switchForm("LANGUAGES")  # Переключаемся на форму LANGUAGES
            case _:
                npyscreen.notify_confirm(f"Action '{action}' is not implemented!")

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

        self.menu_buttons = load_buttons_from_config("./main_menu/mainmenu.json")
        add_buttons_to_menu(self.menu, self.menu_buttons)
        self.menu2_buttons = load_buttons_from_config("./languages/languages_config.json")
        add_buttons_to_menu(self.menu2, self.menu2_buttons)

        
    def handle_menu_selection(self):
        """
        Обрабатывает выбор кнопки в меню.
        """
        action2 = self.menu2_buttons[self.menu2.value].get("action")  # Получаем действие
        
        match action2:
            case "language_cancel":
                self.parentApp.switchForm("MAIN")
            case _:
                npyscreen.notify_confirm(f"Action '{action}' is not implemented!")


if __name__ == "__main__":
    app = MyApp()
    app.run()
