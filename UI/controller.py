import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_crea_grafo(self, e):
        try:
            anno = int(self.view.txt_anno.value)
            if anno < 1871 or anno > 2019:
                self.view.create_alert("Anno non presente nel database")
                return
        except ValueError:
            self.view.create_alert("Inserire un anno")
            return
        try:
            salario = float(self.view.txt_salario.value)*(10**6)
        except ValueError:
            self.view.create_alert("Inserire un salario")
            return
        graph = self.model.build_graph(anno, salario)
        self.able_buttons()
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(
            ft.Text(f"Grafo creato: {len(graph.nodes)} nodi, {len(graph.edges)} archi"))
        self.view.update_page()

    def able_buttons(self):
        self.view.btn_grado.disabled = False
        self.view.btn_connesse.disabled = False
        self.view.btn_team.disabled = False

    def handle_max_grado(self, e):
        nodo_max, grado = self.model.get_max_degree()
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"Il nodo di grado massimo è:"))
        self.view.txt_result.controls.append(ft.Text(f"{nodo_max} --> Grado: {grado}"))
        self.view.update_page()

    def handle_connesse(self, e):
        n_connesse = self.model.get_n_connesse()
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"Il grafo ha {n_connesse} componenti connesse"))
        self.view.update_page()

    def handle_dream_team(self, e):
        dream_team, salario = self.model.get_dream_team()
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"Ecco il dream team, con un salario di {salario/10**6} M$:"))
        for player in dream_team:
            self.view.txt_result.controls.append(ft.Text(player))
        self.view.update_page()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model
