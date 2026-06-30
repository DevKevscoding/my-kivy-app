from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        layout = MDBoxLayout(orientation="vertical", padding=50)

        btn = MDRaisedButton(
            text="App KivyMD OK 🚀",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        layout.add_widget(btn)
        return layout


MyApp().run()