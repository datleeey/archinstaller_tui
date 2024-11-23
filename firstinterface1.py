import npyscreen

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm)

class MainForm(npyscreen.Form):
    def create(self):
        # First menu
        self.menu = self.add(
            npyscreen.BoxTitle,
            name="Arch Install",
            max_width=30,
            max_height=15,
            relx=1,  # X-coordinate for the menu
            rely=1,  # Y-coordinate for the menu
        )

        # Second menu
        self.menu2 = self.add(
            npyscreen.BoxTitle,
            name="Additional Options",
            max_width=50,
            max_height=15,
            relx=33,  # Place this menu to the right of the first menu
            rely=1,   # Same Y-coordinate as the first menu
        )

        # Options for the first menu
        self.menu_buttons = [
            {"name": "Languages", "action": self.action_select_languages},
            {"name": "Keyboard Layout", "action": self.action_keyboard_layout},
            {"name": "Disk Setup", "action": self.action_disk_setup},
        ]

        # Add options dynamically to the first menu
        self.menu.entry_widget.values = [button["name"] for button in self.menu_buttons]
        self.menu.entry_widget.when_value_edited = self.on_menu1_select

        # Prepare storage for second menu actions
        self.menu2_buttons = []

    # First menu selection handler
    def on_menu1_select(self, *args):
        selected_index = self.menu.entry_widget.value
        if selected_index is not None:
            selected_button = self.menu_buttons[selected_index]
            selected_button["action"]()

    # Actions for the first menu
    def action_select_languages(self):
        # Define a list of languages
        languages = [
            {"name": "English", "action": self.language_action_english},
            {"name": "Russian", "action": self.language_action_russian},
            {"name": "Add more languages later...", "action": self.language_action_placeholder},
        ]

        # Update second menu with language options
        self.menu2_buttons = languages
        self.menu2.entry_widget.values = [lang["name"] for lang in languages]
        self.menu2.entry_widget.when_value_edited = self.on_menu2_select
        self.menu2.display()  # Refresh the second menu to show the updated list

    # Second menu selection handler
    def on_menu2_select(self, *args):
        selected_index = self.menu2.entry_widget.value
        if selected_index is not None:
            selected_button = self.menu2_buttons[selected_index]
            selected_button["action"]()

    # Language-specific actions
    def language_action_english(self):
        npyscreen.notify_confirm("You selected: English", title="Language")

    def language_action_russian(self):
        npyscreen.notify_confirm("You selected: Russian", title="Language")

    def language_action_placeholder(self):
        npyscreen.notify_confirm("Other languages will be added later...", title="Language")

    def action_keyboard_layout(self):
        npyscreen.notify_confirm("Selected: Keyboard Layout", title="Action")

    def action_disk_setup(self):
        npyscreen.notify_confirm("Selected: Disk Setup", title="Action")


if __name__ == "__main__":
    app = MyApp()
    app.run()
