import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.page = page
        self.page.title = "Template application using MVC and DAO"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_anno = None
        self.txt_salario = None
        self.btn_grafo = None
        self.btn_connesse = None
        self.btn_grado = None
        self.btn_team = None
        self.txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self.page.controls.append(self._title)

        self.txt_anno = ft.TextField(label="Anno")
        self.txt_salario = ft.TextField(label="Salario (M$)")
        self.btn_grafo = ft.ElevatedButton(text="Crea grafo", on_click=self.controller.handle_crea_grafo)
        row1 = ft.Row([self.txt_anno, self.txt_salario, self.btn_grafo], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row1)

        self.btn_connesse = ft.ElevatedButton(text="Calcola connesse",
                                              disabled=True,
                                              on_click=self.controller.handle_connesse)
        self.btn_grado = ft.ElevatedButton(text="Grado massimo",
                                           disabled=True,
                                           on_click=self.controller.handle_max_grado)
        self.btn_team = ft.ElevatedButton(text="Dream team",
                                          disabled=True,
                                          on_click=self.controller.handle_dream_team)
        row2 = ft.Row([self.btn_connesse, self.btn_grado, self.btn_team], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.page.controls.append(self.txt_result)
        self.page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def update_page(self):
        self.page.update()
