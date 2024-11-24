

def add_buttons_to_menu(self):
        """
        Добавляет кнопки из конфигурации в меню.
        """
        for button in self.menu_buttons:
            self.menu.values.append(button["name"])