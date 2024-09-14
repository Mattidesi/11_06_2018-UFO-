import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.choise_anno=None
        self.choise_stato = None

    def fillDDAnno(self):
        anni=self._model.getAnni()
        for anno, num in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(text=f"{anno}({num})", data=int(anno), on_click=self.readDDAnno))

    def readDDAnno(self, e):
        if e.control.data==None:
            self.choise_anno=None
            return
        self.choise_anno=e.control.data

    def handle_graph(self, e):
        pass

    def handle_countedges(self, e):
        pass

    def handle_search(self, e):
        pass

    def handle_avvistamenti(self, e):
        self._model.buildGraph(self.choise_anno)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di vertici: {self._model.getNumNodes()} Numero di archi: {self._model.getNumEdges()}"))
        self.fillDDStati()
        self._view.update_page()

    def fillDDStati(self):
        stati=self._model.getStati()
        for stato in stati:
            self._view._ddStato.options.append(ft.dropdown.Option(text=stato, data=stato, on_click=self.readDDStato))

    def readDDStato(self, e):
        if e.control.data==None:
            self.choise_stato=None
        self.choise_stato=e.control.data

    def handle_analizza(self, e):
        successori=self._model.getSuccessors(self.choise_stato)
        self._view.txt_result.controls.append(ft.Text("Nodi successori:"))
        for succ in successori:
            self._view.txt_result.controls.append(ft.Text(f"{succ}"))
        predecessori=self._model.getPredecessors(self.choise_stato)
        self._view.txt_result.controls.append(ft.Text("Nodi predecessori:"))
        for pred in predecessori:
            self._view.txt_result.controls.append(ft.Text(f"{pred}"))
        comp_connessa=self._model.getConnessa(self.choise_stato)
        self._view.txt_result.controls.append(ft.Text(f"Nodi raggungibili {len(comp_connessa)}:"))
        for nodo in comp_connessa:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()


    def handle_sequenza(self, e):
        percorso=self._model.getPercorso(self.choise_stato)
        self._view.txt_result.controls.append(ft.Text(f"Percorso migliore:({len(percorso)} nodi attrvarsati)"))
        for nodo in percorso:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()
