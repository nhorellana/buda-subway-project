import sys

class Node:
    """
    This is a class for a subway station represented in a Node structure where
    we can store its name, color and neighbors. This will hellp us to
    find the shortest path between two stations in the future.
    Attributes:
        name (str): Subway station's name. Generally it will be represented as a single letter
        color (str): Represents the color of the station. Can be red, green or mix
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.neighbors = []
        self.prev = None
        self.visited = False

    def add_neighbor(self, node):
        """Undirected graph, so all connections must be bidirectionals"""
        self.neighbors.append(node)
        node.neighbors.append(self)

    def __repr__(self):
        return self.name


class ShortestPath:
    """
    This is a class used to fin de shortest path in a undirected graph between two nodes. 
    It uses the nodes neighbors, prev and visited attributes to travel thorugh the graph
    following a BFS alogrithm.
    Attributes:
        start (Node): Starting Node from where we want to find the shortest path
        end (Node): Ending Node
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def bfs(self):
        """Implementation of a BFS type algoritm to find the shortest path using
        the information of the nodes stored in the ShortestPath class"""
        queue = []
        self.start.visited = True
        queue.append(self.start)
        while queue:
            current_node = queue.pop(0)
            for node in current_node.neighbors:
                if not node.visited:
                    node.visited = True
                    queue.append(node)
                    node.prev = current_node
                    if node == self.end:
                        queue.clear()
                        break
        # BFS completed, now trace the route
        self.trace_route()
    
    def trace_route(self):
        """ Function to trace the route using preceding nodes"""
        node = self.end
        route = []
        while node:
            route.append(node)
            node = node.prev
        route.reverse()
        if len(route) == 1:
            print("Imposible, estación de inicio o término no calza con el color de tren seleccionado")
            sys.exit()
        shortest_path = ''
        for node in route:
            if node.name == self.end.name:
                shortest_path += node.name
            else:
                shortest_path += node.name
                shortest_path += '->'
        print(shortest_path)
