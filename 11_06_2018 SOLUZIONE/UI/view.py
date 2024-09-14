import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None

        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None

        self.txt_container = None
        self._ddAnno=None
        self._btn_avvistamenti=None
        self._ddStato=None
        self._btn_analizza=None
        self._btn_sequenza=None


    def load_interface(self):
        # title
        self._title = ft.Text("29/06/2022 Turno A", color="blue", size=24)
        self._page.controls.append(self._title)

        #row1
        self._ddAnno=ft.Dropdown(label="Anno")
        self._btn_avvistamenti=ft.ElevatedButton(text="Avvistamenti", on_click=self._controller.handle_avvistamenti)
        row1=ft.Row([self._ddAnno, self._btn_avvistamenti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # row2
        self._ddStato = ft.Dropdown(label="Stato")
        self._btn_analizza= ft.ElevatedButton(text="Analizza", on_click=self._controller.handle_analizza)
        row2 = ft.Row([self._ddStato, self._btn_analizza], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #row3
        self._btn_sequenza = ft.ElevatedButton(text="Sequenza avvistamenti", on_click=self._controller.handle_sequenza)
        self._page.controls.append(self._btn_sequenza)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._controller.fillDDAnno()
        self._page.update()

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
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
