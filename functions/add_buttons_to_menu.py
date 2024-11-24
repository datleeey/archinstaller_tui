def add_buttons_to_menu(menu, buttons):
    """
    Добавляет кнопки из конфигурации в указанное меню.
    """
    if not isinstance(buttons, list):
        raise ValueError("Buttons must be a list.")

    for button in buttons:
        if "name" in button:
            menu.values.append(button["name"])
        else:
            raise ValueError("Each button must have a 'name' key.")
    menu.display()
