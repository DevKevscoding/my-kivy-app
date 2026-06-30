from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        screen = MDScreen()

        layout = MDBoxLayout(
            orientation="vertical",
            padding=50,
            spacing=20
        )

        title = MDLabel(
            text="🚀 KivyMD App Ready",
            halign="center",
            font_style="H4"
        )

        btn = MDRaisedButton(
            text="Click Me",
            pos_hint={"center_x": 0.5}
        )

        btn.bind(on_release=self.on_click)

        layout.add_widget(title)
        layout.add_widget(btn)

        screen.add_widget(layout)
        return screen

    def on_click(self, instance):
        print("Button clicked!")

MainApp().run()