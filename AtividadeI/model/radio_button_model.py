from button_model import Button


class RadioButton(Button):
    checked = False


    def checked(self, checked):
        """
            Função checked.
        """
        self.checked = checked