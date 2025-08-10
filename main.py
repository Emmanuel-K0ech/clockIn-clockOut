# # # from kivy.app import App
# # # from kivy.uix.boxlayout import BoxLayout
# # # from kivy.uix.button import Button
# # # from kivy.uix.label import Label
# # # from kivy.uix.widget import Widget
# # # from kivy.uix.screenmanager import ScreenManager, Screen
# # # import datetime


# # # clockInTime = '0000-00-00 00:00:00'  # Global variable to store clock-in time

# # # class MyWidget(Screen):
# # #     def on_button_click(self):
# # #         global clockInTime
# # #         clockInTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # #         print(f"Clocked In at: {clockInTime}")


# # #     def on_button_click2(self, instance):
# # #         clockOutTime = datetime.datetime.now()
# # #         global clockInTime
# # #         hrsWorked = clockOutTime - datetime.datetime.strptime(clockInTime, "%Y-%m-%d %H:%M:%S")
# # #         hrsWorked = hrsWorked.total_seconds() / 3600  # Convert seconds to hours
# # #         print(f"Clocked Out at: {clockOutTime.strftime('%Y-%m-%d %H:%M:%S')}")
# # #         print(f"Hours worked: {hrsWorked:.2f} hours")

# # # class MyApp(App):
# # #     def build(self):
# # #         my_widget = MyWidget()
# # #         my_widget.add_widget(Button(text='Clock In', on_release=my_widget.on_button_click))
# # #         my_widget.add_widget(Button(text='Clock Out', on_release=my_widget.on_button_click2))   
# # #         return my_widget

# # # if __name__ == '__main__':
# # #     MyApp().run()
# # from kivymd.app import MDApp
# # from kivymd.uix.label import MDLabel
# # from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
# # from kivymd.uix.screen import MDScreen
# # from kivymd.uix.boxlayout import MDBoxLayout
# # from kivy.lang import Builder


# # class MainApp(MDApp):
# #     def build(self):
# #         return Builder.load_file('main.kv')


# # MainApp().run()

# # # The above code is a simple Kivy application that uses the KivyMD library for Material Design components.
# # # It sets the theme to dark mode and uses a blue-gray color palette.
# # # The application will load the user interface from a KV file named 'myapp.kv'.
# # # Make sure to create the 'myapp.kv' file in the same directory with the appropriate UI definitions.
# # # The application can be run by executing this script, which will start the Kivy event loop and display the UI defined in 'myapp.kv'.
# # # Ensure you have Kivy and KivyMD installed in your Python environment to run this application successfully.
# # # You can install them using pip:
# # # pip install kivy kivymd
# # # This code is a basic template for a Kivy application and can be extended with more functionality
# # # by adding more widgets and logic in the KV file or in the Python code.


# from kivy.lang import Builder
# from kivy.properties import StringProperty

# from kivymd.app import MDApp
# from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
# from kivymd.uix.screen import MDScreen


# class BaseMDNavigationItem(MDNavigationItem):
#     icon = StringProperty()
#     text = StringProperty()


# class BaseScreen(MDScreen):
#     image_size = StringProperty()


# KV = '''
# <BaseMDNavigationItem>

#     MDNavigationItemIcon:
#         icon: root.icon

#     MDNavigationItemLabel:
#         text: root.text


# <BaseScreen>

#     FitImage:
#         source: f"https://picsum.photos/{root.image_size}/{root.image_size}"
#         size_hint: .9, .9
#         pos_hint: {"center_x": .5, "center_y": .5}
#         radius: dp(24)


# MDBoxLayout:
#     orientation: "vertical"
#     md_bg_color: self.theme_cls.backgroundColor

#     MDScreenManager:
#         id: screen_manager

#         BaseScreen:
#             name: "Screen 1"
#             image_size: "1024"

#         BaseScreen:
#             name: "Screen 2"
#             image_size: "800"

#         BaseScreen:
#             name: "Screen 3"
#             image_size: "600"


#     MDNavigationBar:
#         on_switch_tabs: app.on_switch_tabs(*args)

#         BaseMDNavigationItem
#             icon: "gmail"
#             text: "Screen 1"
#             active: True

#         BaseMDNavigationItem
#             icon: "twitter"
#             text: "Screen 2"

#         BaseMDNavigationItem
#             icon: "linkedin"
#             text: "Screen 3"
# '''


# class Example(MDApp):
#     def on_switch_tabs(
#         self,
#         bar: MDNavigationBar,
#         item: MDNavigationItem,
#         item_icon: str,
#         item_text: str,
#     ):
#         self.root.ids.screen_manager.current = item_text

#     def build(self):
#         return Builder.load_string(KV)


# Example().run()

from cin_out import clockInOut
import time


testFunc = clockInOut()
clock_in_time = testFunc.clock_in()
time.sleep(30)
clock_out_time = testFunc.clock_out()
testFunc.calculate_hours_worked(clock_in_time, clock_out_time)