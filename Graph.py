import networkx as nx
import matplotlib.pyplot as plt
import include

# robotL = include.Generator.create_master(include.robotL_states, include.robotL_transitions)
# print(robotL.current_state.name)


G = nx.DiGraph()
W_cz_w_s_r = "Wjazd czesci w strefe robocza"
states = {0: "Wjazd czesci w strefe robocza", 1: "Spowolnienie tasmy", 2: "Zatrzymanie tasmy i zamkniecie zatrzaskow",
          3: "Zezwolenie na prace", 4: "Sprawdzenie pozycji robota",
          5: "Wylaczenie zezwolenian prace robota i zwolnienie zatrzaskow", 6: "Wlaczenie tasmy",
          1_0: "RPozycja domowa",
          1_1: "RSekwencja 1", 1_2: "RSekwencja 2", 1_3: "RPrzygotowanie do ponownego wykonania",
          2_0: "LPozycja domowa",
          2_1: "LSekwencja 1", 2_2: "LSekwencja 2", 2_3: "LPrzygotowanie do ponownego wykonania"}

path_states = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0), (4, 1_0), (1_0, 1_1), (1_1, 1_2),
               (1_2, 1_0),
               (4, 2_0), (2_0, 2_1), (2_1, 2_2), (2_2, 2_0), (1_1, 1_3), (1_2, 1_3), (1_3, 1_0), (2_1, 2_3), (2_2, 2_3),
               (2_3, 2_0)]
G.add_nodes_from(states)
G.add_edges_from(path_states)
H = nx.relabel_nodes(G, states, copy=False)

print("Nodes of graph: ")
print(H.nodes())
print("Edges of graph: ")
print(H.edges())
nx.draw(H, with_labels=True)
plt.savefig("path_graph_cities.png")
plt.show()
