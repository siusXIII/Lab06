import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab 06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddAnno = None
        self.ddBrand = None
        self.ddRetailer = None
        self.btnPrintTopVendite = None
        self.btnPrintAnalizzaVendite = None
        self.txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some Dropdown
        # ROW 1

        self.ddAnno = ft.Dropdown(label="Anno", width=200, options=[ft.dropdown.Option("Nessuno filtro!")])
        self._controller.fillDDAnno()

        self.ddBrand = ft.Dropdown(label="Brand", width=200, options=[ft.dropdown.Option("Nessuno filtro!")])
        self._controller.fillDDBrand()

        self.ddRetailer = ft.Dropdown(label="Retailer", width=450, options=[ft.dropdown.Option("Nessuno filtro!")])
        self._controller.fillDDRetailer()

        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer], alignment=ft.MainAxisAlignment.CENTER)

        # bottoni per Top Vendite e Analisi Vendite

        self.btnPrintTopVendite = ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handlePrintTopVendite)
        self.btnPrintAnalizzaVendite = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handlePrintAnalizzaVendite)

        row2 = ft.Row([self.btnPrintTopVendite, self.btnPrintAnalizzaVendite], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
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
