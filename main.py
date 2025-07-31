from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
import datetime


clockInTime = None  # Global variable to store clock-in time

class MyWidget(Screen):
    def on_button_click(self):
        global clockInTime
        clockInTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Clocked In at: {clockInTime}")


    def on_button_click2(self):
        clockOutTime = datetime.datetime.now()
        hrsWorked = clockOutTime - datetime.datetime.strptime(clockInTime, "%Y-%m-%d %H:%M:%S")
        hrsWorked = hrsWorked.total_seconds() / 3600  # Convert seconds to hours
        print(f"Clocked Out at: {clockOutTime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Hours worked: {hrsWorked:.2f} hours")

    class MainScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            layout = BoxLayout(orientation='vertical')
            layout.add_widget(Label(text='Welcome to the Main Screen!'))
            btn = Button(text='Go to Second Screen')
            btn.bind(on_release=self.go_to_second_screen)
            layout.add_widget(btn)
            self.add_widget(layout)

        def go_to_second_screen(self, instance):
            self.manager.current = 'second_screen'

    class SecondScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            layout = BoxLayout(orientation='vertical')
            layout.add_widget(Label(text='This is the Second Screen!'))
            btn = Button(text='Go back to Main Screen')
            btn.bind(on_release=self.go_to_main_screen)
            layout.add_widget(btn)
            self.add_widget(layout)

        def go_to_main_screen(self, instance):
            self.manager.current = 'main_screen'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyWidget.MainScreen(name='main_screen'))
        sm.add_widget(MyWidget.SecondScreen(name='second_screen'))
        my_widget = MyWidget()
        my_widget.add_widget(Button(text='Clock In', on_release=my_widget.on_button_click))
        my_widget.add_widget(Button(text='Clock Out', on_release=my_widget.on_button_click2))
        sm.add_widget(MyWidget(name='my_widget'))    
        return sm

if __name__ == '__main__':
    MyApp().run()
