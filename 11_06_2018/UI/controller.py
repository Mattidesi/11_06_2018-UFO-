import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDAnno(self):
        self._view._ddAnno.options.clear()

        years = self._model.getYears()

        for year in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(f"{year[0]} - {year[1]}"))
        self._view.update_page()

    def fillDDStati(self,e):
        self._view.txt_result.controls.clear()
        states = self._model.getStates(int(self._view._ddAnno.value[0:5]))

        for state in states:
            self._view._ddStato.options.append(ft.dropdown.Option(state))
            self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        if self._view._ddAnno.value is None:
            self._view.txt_result.controls.append(ft.Text("Inserisci un anno!", color='red'))
            self._view.update_page()
            return

        self._view._ddStato.disabled = False
        self._model.buildGraph(int(self._view._ddAnno.value[0:5]))
        nNodes,nEdges = self._model.getGraphDetails()

        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nNodes}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nEdges}"))
        self._view.update_page()
    def handle_avvistamenti(self, e):
        pass

    def handle_analizza(self, e):
        self._view.txt_result.controls.clear()
        if self._view._ddAnno.value is None or self._view._ddStato.value is None:
            self._view.txt_result.controls.append(ft.Text("Inserisci un anno ed uno stato!", color='red'))
            self._view.update_page()
            return

        pred = self._model.predStato(self._view._ddStato.value)
        succ = self._model.succStato(self._view._ddStato.value)
        self._view.txt_result.controls.append(ft.Text(f"Gli stati precedenti sono:"))
        self._view.update_page()

        for p in pred:
            self._view.txt_result.controls.append(ft.Text(p))
            self._view.update_page()

        self._view.txt_result.controls.append(ft.Text(f"Gli stati successivi sono:"))
        self._view.update_page()

        for s in succ:
            self._view.txt_result.controls.append(ft.Text(s))
            self._view.update_page()


    def handle_sequenza(self, e):
       pass