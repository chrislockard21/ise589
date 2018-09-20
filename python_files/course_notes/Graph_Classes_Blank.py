"""
A Graph implemented with Python Classes and Dictionaries
Adapted from:https://www.python-course.eu/graphs_python.php
Extra Study: How to find the path between 2 nodes in a given graph?

"""

class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def nodes(self):
        return list(self.__graph_dict.keys())

    def arcs(self):
        return self.__generate_arcs()

    def add_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    def add_arc(self, arc):
        (node1, node2) = tuple(arc)
        if node1 in self.__graph_dict:
            self.__graph_dict[node1].append(node2)
        else:
            self.__graph_dict[node1] = [node2]

    def __generate_arcs(self):
        arcs = []
        for node in self.__graph_dict:
            for friend in self.__graph_dict[node]:
                if (friend, node) not in arcs:
                    arcs.append((node, friend))
        return arcs

    def __str__(self):
        res = "nodes: "
        for node in self.__graph_dict:
            res += str(node) + " "
        res += "\narcs: "
        for arc in self.__generate_arcs():
            res += str(arc) + " "
        return res


def main():

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : ["e", "b"]
        }

    graph = Graph(g)

    print("Nodes of graph:")
    print(graph.nodes())

    print("Arc of graph:")
    print(graph.arcs())

    print("Add Nodes:")
    graph.add_node("z")

    print("Nodes of graph:")
    print(graph.nodes())

    print("Add an arc:")
    graph.add_arc({"z","a"})

    print("Nodes of graph:")
    print(graph.nodes())

    print("Arc of graph:")
    print(graph.arcs())

    print('Adding an arc ("x","y") with new nodes:')
    graph.add_arc(("x","y"))

    print("Nodes of graph:")
    print(graph.nodes())
    print("Arcs of graph:")
    print(graph.arcs())

    print('The final graph is')
    print(graph)

#main program
main()
