import json
import npyscreen
from languages.functions import *
from forms.funtions import *

class Menu(npyscreen.Form):
    def create(self, config_path):
        self.menu = self.add(
            npyscreen.BoxTitle,
            name="Menu 1",
            max_height=15,
            max_width=30,
            relx=1,
            rely=1,
        )
        self.menu_buttons = load_buttons_from_config(config_path)
        add_buttons_to_menu(self.menu, self.menu_buttons)

        # Назначаем обработчик выбора
        self.menu.when_value_edited = self.on_button_select

    def on_button_select(self, *args):
        selected_index = self.menu.value  # Получаем индекс выбранного элемента
        if selected_index is not None:
            selected_button = self.menu_buttons[selected_index]
            execute_action(selected_button["action"], self)  # Передаем self

    def language_menu_open(self):
        self.parentApp.switchForm('LANGUAGES')

class BaseForm(npyscreen.Form):
    def create(self, config_path, second_config_path):
        self.menu2 = self.add(
            npyscreen.BoxTitle,
            name="Menu 1",
            max_height=15,
            max_width=50,
            relx=33,
            rely=1,
        )
        self.menu = self.add(
            npyscreen.BoxTitle,
            name="Menu 2",
            max_height=15,
            max_width=30,
            relx=1,
            rely=1,
        )

        self.menu_buttons = load_buttons_from_config(config_path)
        add_buttons_to_menu(self.menu, self.menu_buttons)
        self.menu2_buttons = load_buttons_from_config(second_config_path)
        add_buttons_to_menu(self.menu2, self.menu2_buttons)

        self.menu2.when_value_edited = self.on_button_select

    def on_button_select(self, *args):
        selected_index = self.menu2.value  # Получаем индекс выбранного элемента
        if selected_index is not None:
            selected_button = self.menu2_buttons[selected_index]
            execute_action(selected_button["action"], self)  # Передаем self