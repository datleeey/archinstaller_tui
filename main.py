import npyscreen
from forms.createform import BaseForm

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm)
        self.addForm('LANGUAGES', LanguageForm)

class MainForm(BaseForm):
    def create(self):
        return
    
class LanguageForm(BaseForm):
    def create(self):
        return