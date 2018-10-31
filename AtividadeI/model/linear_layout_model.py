from view_group_model import ViewGroup


class LinearLayout(ViewGroup):
    tipo = None


    def tipo(self, tipo):
        """
            Declaramos a forma do layout
        """
        self.tipo = tipo
    