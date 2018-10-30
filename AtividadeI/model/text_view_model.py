from view_model import View


class TextView(View):
    texto = None


    def texto(self, texto):
        """
            Adiciona um texto na view
        """
        self.texto = texto