import npyscreen
import json

def load_buttons_from_config(config_path):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Неверный формат конфигурации. Ожидается список.")
        
        buttons = [{"name": item["name"], "action": item["action"]} for item in data]
        return buttons
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл конфигурации не найден: {config_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка чтения JSON из файла: {config_path}")
    except KeyError as e:
        raise ValueError(f"Ошибка структуры данных в JSON: отсутствует ключ {e}")


def add_buttons_to_menu(menu, buttons):
    menu.values = [button["name"] for button in buttons]
    menu.display()


def execute_action(action_name, form_instance=None):
    """Динамически вызываем функцию по имени."""
    try:
        # Если это метод формы
        if form_instance and hasattr(form_instance, action_name):
            getattr(form_instance, action_name)()
        else:
            # Ищем глобальную функцию
            action_function = globals().get(action_name)
            if callable(action_function):
                action_function()  # Вызов глобальной функции
            else:
                npyscreen.notify_confirm(
                    f"Действие '{action_name}' не найдено!",
                    title="Ошибка"
                )
    except Exception as e:
        npyscreen.notify_confirm(
            f"Ошибка при выполнении действия: {str(e)}",
            title="Ошибка"
        )