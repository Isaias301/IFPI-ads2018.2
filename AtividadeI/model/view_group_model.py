from view_model import View


class ViewGroup(View):
    layout = False
    view = []


    def view(self, view):
        """
            Adiciona views a Class ViewGroup. A mesma e um conjunto de view
        """
        self.view.append(view)