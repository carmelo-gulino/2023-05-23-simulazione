import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.best_salario = None
        self.best_sol = None
        self.graph = nx.Graph()
        self.players = []
        self.players_map = {}
        self.appearances = {}

    def build_graph(self, anno, salario):
        self.graph.clear()
        self.players = DAO.get_players(anno, salario)
        self.players_map = {p.playerID: p for p in self.players}
        self.graph.add_nodes_from(self.players)
        self.appearances = DAO.get_appearances(anno, salario)
        for u in self.graph.nodes:
            for v in self.graph.nodes:
                if u != v:
                    try:
                        for team in self.appearances[u.playerID]:
                            if team in self.appearances[v.playerID]:
                                self.graph.add_edge(u, v)
                    except KeyError:
                        pass
        return self.graph

    def get_max_degree(self):
        degrees = list(nx.degree(self.graph))
        degrees.sort(key=lambda x: x[1], reverse=True)
        return degrees[0][0], degrees[0][1]

    def get_n_connesse(self):
        return nx.number_connected_components(self.graph)

    def get_dream_team(self):
        self.best_sol = []
        self.best_salario = 0
        for player in self.graph.nodes:
            parziale = [player]
            salari = [player.tot_salary]
            self.ricorsione(parziale, salari)
        return self.best_sol, self.best_salario

    def ricorsione(self, parziale, salari):
        salario_tot = salari[-1]
        ultimo = parziale[-1]
        if salario_tot > self.best_salario:
            self.best_sol = copy.deepcopy(parziale)
            self.best_salario = copy.deepcopy(salario_tot)
            print(parziale)
        for neighbor in self.graph.neighbors(ultimo):
            if self.check(parziale, ultimo, neighbor):
                parziale.append(neighbor)
                salari.append(salario_tot + neighbor.tot_salary)
                self.ricorsione(parziale, salari)
                parziale.pop()
                salari.pop()

    def check(self, parziale, ultimo, neighbor):
        if neighbor in parziale:
            return False
        for team in self.appearances[neighbor.playerID]:
            if team in self.appearances[ultimo.playerID]:
                return False
        return True
