# Test express line, test normal line

# assert equal (verdes no tienen conexiones)
# normal line connections == neighbors de cada nodo

import unittest

from functions import express_line, non_express

MEDIUM = {
    "A": {
        "color": "mix",
        "vecinos": ["B"]
    },
    "B": {
        "color": "mix",
        "vecinos": ["A", "C","G"]
    },
    "C": {
        "color": "green",
        "vecinos": ["B", "D"]
    },
    "D": {
        "color": "red",
        "vecinos": ["C","E"]
    },
    "E": {
        "color": "mix",
        "vecinos": ["D","K","F"]
    },
    "F": {
        "color": "mix",
        "vecinos": ["E"]
    },
    "G": {
        "color": "red",
        "vecinos": ["B","H"]
    },
    "H": {
        "color": "green",
        "vecinos": ["G","I"]
    },
    "I": {
        "color": "mix",
        "vecinos": ["H","J","L"]
    },
    "J": {
        "color": "green",
        "vecinos": ["I","K"]
    },
    "K": {
        "color": "red",
        "vecinos": ["J", "E"]
    },
    "L": {
        "color": "red",
        "vecinos": ["I", "M"]
    },
    "M": {
        "color": "mix",
        "vecinos": ["L"]
    }
}

class TestFunctions(unittest.TestCase):
    def test_express_line_red(self):
        """
        Test that if the express line returns a dict of nodes with
        the expectetd ammount of connections depending of color.
        If colour equals 'red', green nodes should have no connections in the graph
        If colour equals 'green', red nodes should have no connections in the graph
        """
        expected_nodes_without_connections_red = ['C', 'H', 'J']
        nodes_without_connections = []
        nodes_red = express_line(MEDIUM, 'red')
        for node in nodes_red.items():
            name, node_class = node
            if not node_class.neighbors:
                nodes_without_connections.append(name)
        self.assertEqual(nodes_without_connections,
                         expected_nodes_without_connections_red)

    def test_express_line_green(self):
        expected_nodes_without_connections_green = ['D', 'G', 'K', 'L']
        nodes_without_connections = []
        nodes_green = express_line(MEDIUM, 'green')
        for node in nodes_green.items():
            name, node_class = node
            if not node_class.neighbors:
                nodes_without_connections.append(name)
        self.assertEqual(nodes_without_connections,
                         expected_nodes_without_connections_green)

    def test_non_express(self):
        """
        Test that if the non express line returns a dict of nodes with
        the expectetd ammount of connections.
        """
        expected_nodes_without_connections_mixed = []
        nodes_without_connections = []
        nodes_mixed = non_express(MEDIUM)
        for node in nodes_mixed.items():
            name, node_class = node
            if not node_class.neighbors:
                nodes_without_connections.append(name)
        self.assertEqual(nodes_without_connections,
                         expected_nodes_without_connections_mixed)

if __name__ == '__main__':
    unittest.main()
