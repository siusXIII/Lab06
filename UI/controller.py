import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._retailerCode = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDAnno(self):
        for a in self._model.getAllAnni():
            self._view.ddAnno.options.append(ft.dropdown.Option(a))

    def fillDDBrand(self):
        for b in self._model.getAllBrand():
            self._view.ddBrand.options.append((ft.dropdown.Option(b)))

    def fillDDRetailer(self):
        for r in self._model.getAllRetailer():
            self._view.ddRetailer.options.append((ft.dropdown.Option(key=r.Retailer_name,
                                                                     data=r,
                                                                     on_click=self.read_retailer)))

    def read_retailer(self,e):
        if e.control.data is None:
            self._retailerCode = None
        else:
            self._retailerCode = e.control.data


    def handlePrintTopVendite(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view.ddAnno.value
        brand = self._view.ddBrand.value
        retailer = self._view.ddRetailer.value
        if anno is None:
            self._view.create_alert("Attenzione, selezionare un anno!")
            self._view.update_page()
            return
        if brand is None:
            self._view.create_alert("Attenzione, selezionare un brand!")
            self._view.update_page()
            return
        if retailer is None:
            self._view.create_alert("Attenzione, selezionare un retailer!")
            self._view.update_page()
            return

        if anno == "Nessuno filtro!":
            anno = "null"
        if brand == "Nessuno filtro!":
            brand = "null"
        if retailer == "Nessuno filtro!":
            retailer = "null"

        ricavi = self._model.getRicavi(anno,brand,retailer)

        for r in ricavi:
            self._view.txt_result.controls.append(ft.Text(r))
        self._view.update_page()


    def handlePrintAnalizzaVendite(self,e):
        pass