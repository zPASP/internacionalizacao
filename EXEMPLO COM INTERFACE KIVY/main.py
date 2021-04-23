from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import gettext


#gettext.bindtextdomain('main', '/locale')
#gettext.textdomain('main')
t = gettext.translation('main', localedir='locale', languages=['paspa'], fallback=True)
#t.install()
_ = t.gettext



class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text=(_('User Name'))))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text=(_('password'))))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
