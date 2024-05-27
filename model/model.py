import itertools
import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.allTeams=[]
        self.grafo=nx.Graph()
        pass

    def getYears(self):
        return DAO.getAllYears()

    def buildGraph(self):
        self.grafo.clear()
        if len(self.allTeams)==0:
            print("attenzione non ci sono squadre")
            return

        self.grafo.add_nodes_from(self.allTeams)

        myedges= list(itertools.combinations(self.allTeams,2))
        self.grafo.add_edges_from(myedges)

        # for t1 in self.grafo.nodes:
        #     for t2 in self.grafo.nodes:
        #         if t1!=t2:
        #             self.grafo.add_edge(t1,t2)


    def printGraphDetails(self):
        print(f"Grafo creato con {len(self.grafo.nodes)} nodi e {len(self.grafo.edges)} archi")

    def getTeamsOfYear(self,anno):
        self.allTeams=DAO.getTeamsOfYear(anno)
        return self.allTeams
