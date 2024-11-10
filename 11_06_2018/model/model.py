import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.nodes = []
        self.idMap = {}
        self.name_to_id = {}

    def getYears(self):
        return DAO.getYears()

    def buildGraph(self,year):
        self.nodes = DAO.getAllNodes(year)
        self.grafo.add_nodes_from(self.nodes)

        for node in self.grafo.nodes:
            self.idMap[node.id] = node

        edges = DAO.getAllEdges(year,self.idMap)

        for edge in edges:
            if self.grafo.has_edge(edge.s1,edge.s2):
                pass
            else:
                self.grafo.add_edge(edge.s1,edge.s2)


    def getGraphDetails(self):
        return len(self.grafo.nodes),len(self.grafo.edges)


    def getStates(self,year):
        states =   DAO.getStates(year)

        for state in states:
            self.name_to_id[state.Name] = state
            print(self.name_to_id[state.Name])

        return states


    def predStato(self,name):
        v0 = self.name_to_id[name]
        pred = nx.dfs_predecessors(self.grafo,v0)
        allPred = []

        for v in pred.values():
            allPred.append(v)

        return allPred

    def succStato(self,name):
        v0 = self.name_to_id[name]
        succ = nx.dfs_successors(self.grafo,v0)
        allSucc= []

        for v in succ.values():
            allSucc.extend(v)

        return allSucc