import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=nx.DiGraph()
        self.lista_nodi=[]
        self.best_path=[]



    def buildGraph(self, anno):
        self.grafo.clear()
        self.lista_nodi=DAO.getNodes(anno)
        self.grafo.add_nodes_from(self.lista_nodi)
        archi=DAO.getEdges(anno)
        for s1, s2 in archi:
            if s1!=s2:
                self.grafo.add_edge(s1, s2)

    def getAnni(self):
        anni= DAO.getAllYears()
        return anni

    def getStati(self):
        return self.lista_nodi

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def getSuccessors(self, stato):
        if stato not in self.grafo.nodes:
            return
        return list(self.grafo.successors(stato))


    def getPredecessors(self, stato):
        if stato not in self.grafo.nodes:
            return
        return list(self.grafo.predecessors(stato))
    def getConnessa(self, stato):
        connessa=[]
        for nodo in self.lista_nodi:
            if nodo!=stato and nx.has_path(self.grafo, stato, nodo):
                connessa.append(nodo)
        return connessa

    def getPercorso(self, statoP):
        self.best_path = []
        self.ricorsione([statoP])
        return self.best_path

    def ricorsione(self, parziale):
        #controllo se la soluzione è migliore di best
        if len(parziale) >len(self.best_path):
            self.best_path = copy.deepcopy(parziale)

        #continuo ad aggiungere nodi
        for nodo in self.grafo.successors(parziale[-1]):
            if nodo not in parziale:
                parziale.append(nodo)
                self.ricorsione(parziale)
                #backtacking
                parziale.pop()


