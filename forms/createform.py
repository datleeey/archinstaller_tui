import json
import npyscreen

def load_buttons_from_config(config_path):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            raise ValueError("Неверный формат конфигурации. Ожидается список.")
        
        # Преобразуем каждый элемент в нужный формат
        buttons = [{"name": item["name"], "action": item["action"]} for item in data]
        return buttons
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл конфигурации не найден: {config_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка чтения JSON из файла: {config_path}")
    except KeyError as e:
        raise ValueError(f"Ошибка структуры данных в JSON: отсутствует ключ {e}")


# Функция для добавления кнопок в меню
def add_buttons_to_menu(menu, buttons):
    menu.values = [button["name"] for button in buttons]
    menu.display()


# Класс MainForm
class BaseForm(npyscreen.Form):
    def __init__(self, menu_count, menu_config_path_1, menu_config_path_2=None, *args, **kwargs):
        if menu_count < 1 or menu_count > 2:
            raise ValueError("Ты дурак? Максимум два меню!")
        
        # Сохраняем параметры для использования в методе `create`
        self.menu_count = menu_count
        self.menu_config_path_1 = menu_config_path_1
        self.menu_config_path_2 = menu_config_path_2
        super(BaseForm, self).__init__(*args, **kwargs)

    def create(self):
        if self.menu_count == 1:
            # Создаем только первое меню
            self.menu = self.add(
                npyscreen.BoxTitle,
                name="Menu 1",
                max_height=15,
                max_width=30,
                relx=1,
                rely=1,
            )
            self.menu_buttons = load_buttons_from_config(self.menu_config_path_1)
            add_buttons_to_menu(self.menu, self.menu_buttons)
        elif self.menu_count == 2:
            # Создаем оба меню
            self.menu = self.add(
                npyscreen.BoxTitle,
                name="Menu 1",
                max_height=15,
                max_width=30,
                relx=1,
                rely=1,
            )
            self.menu2 = self.add(
                npyscreen.BoxTitle,
                name="Menu 2",
                max_height=15,
                max_width=50,
                relx=33,
                rely=1,
            )
            self.menu_buttons = load_buttons_from_config(self.menu_config_path_1)
            add_buttons_to_menu(self.menu, self.menu_buttons)

            if self.menu_config_path_2:
                self.menu2_buttons = load_buttons_from_config(self.menu_config_path_2)
                add_buttons_to_menu(self.menu2, self.menu2_buttons)

    def handle_menu_selection(self):
        # Пример обработки событий
        npyscreen.notify_confirm(f"Selected option: {self.menu.value}")
