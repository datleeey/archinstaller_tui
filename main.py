import npyscreen
from forms.createform import Menu,BaseForm

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm)
        self.addForm('LANGUAGES', LanguageForm)

class MainForm(Menu):
    def create(self):
        super().create("mainmenu.json")
    
class LanguageForm(BaseForm):
    def create(self):
        return super().create("mainmenu.json", "languages/languages.json")

if __name__ == "__main__":
    app = MyApp()
    app.run()