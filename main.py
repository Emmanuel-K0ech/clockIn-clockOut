from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import datetime


clockInTime = None  # Global variable to store clock-in time

class MyWidget(BoxLayout):
    def on_button_click(self):
        global clockInTime
        clockInTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Clocked In at: {clockInTime}")


    def on_button_click2(self):
        hrsWorked = datetime.datetime.now() - datetime.datetime.strptime(clockInTime, "%Y-%m-%d %H:%M:%S")
        hrsWorked = hrsWorked.total_seconds() / 3600  # Convert seconds to hours
        print(f"Hours worked: {hrsWorked:.2f} hours")
    

class MyApp(App):
    def build(self):
        return MyWidget()

MyApp().run()
