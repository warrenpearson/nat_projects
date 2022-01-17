"""
Buttons App
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT


class Buttons(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        nat_button = toga.Button(
            "Nat says",
            on_press=self.nat_says,
            style=Pack(padding=(10, 20), width=200, alignment="right"),
        )

        dad_button = toga.Button(
            "Dad says",
            on_press=self.dad_says,
            style=Pack(padding=(10, 20), width=100, alignment="right"),
        )

        mum_button = toga.Button(
            "Mum says",
            on_press=self.mum_says,
            style=Pack(padding=(10, 20), width=100, alignment="right"),
        )

        self.nat_label = toga.Label(
            ".....", style=Pack(padding=(10, 20), width=200, text_align=LEFT)
        )
        self.mum_label = toga.Label(
            ".....", style=Pack(padding=(10, 20), width=200, text_align=LEFT)
        )
        self.dad_label = toga.Label(
            ".....", style=Pack(padding=(10, 20), width=200, text_align=LEFT)
        )

        main_box.add(nat_button)
        main_box.add(self.nat_label)
        main_box.add(mum_button)
        main_box.add(self.mum_label)
        main_box.add(dad_button)
        main_box.add(self.dad_label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def nat_says(self, widget):
        self.nat_label.text = "I'll just have a little rest"

    def dad_says(self, widget):
        self.dad_label.text = "I'm coming up in a second"

    def mum_says(self, widget):
        self.mum_label.text = "Like with like!"


def main():
    return Buttons()
