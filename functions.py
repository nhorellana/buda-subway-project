from entities import Node


def parser(file, color):
    """
    Function that redirects the subway network information
    to the corresponding function depending of the trains colour.
    """
    if color in ['red', 'green']:
        nodes = express_line(file, color)
    else:
        nodes = non_express(file)
    return nodes


def express_line(file, color):
    """Function that recibes a dict type structure with the
    whole subway network information and the color (str) of the train.
    With this information we filter it using only the stations
    that work with the selected color. Finally we connect all the nodes with its
    corresponding neighbors and return a dictionary structure with the resulting
    graph"""
    nodes_str_to_object = {} # {'A': A}
    connections_node_neighbors = {}
    for tuple_node_name_data in file.items():
        node_name, node_data = tuple_node_name_data # node_data = {color: str(), vecinos: []}
        nodes_str_to_object[node_name] = Node(
            node_name, node_data["color"])
        connections_node_neighbors[node_name] = node_data["vecinos"]
    # tuple_node_stations = (Node_name str, Neighbors [])
    for tuple_node_stations in connections_node_neighbors.items():
        node_name, neighbors = tuple_node_stations
        if nodes_str_to_object[node_name].color in [color, 'mix']:
            for node in neighbors:
                if nodes_str_to_object[node].color in [color, 'mix']:
                    if nodes_str_to_object[node] not in nodes_str_to_object[node_name].neighbors:
                        nodes_str_to_object[node_name].add_neighbor(
                            nodes_str_to_object[node])
                # If neighbor's colour is diferent that the one we selected, we select the first of its neighbor's
                # and add it to the parent node.
                else:
                    next_eval = list(
                        filter(lambda node: node != node_name, connections_node_neighbors[node]))[0]
                    if next_eval not in nodes_str_to_object[node].neighbors:
                        neighbors.append(next_eval)
    return nodes_str_to_object


def non_express(file):
    """Function that recibes a dict type structure with the
    whole subway network information so we connect all the nodes with its
    corresponding neighbors and return a dictionary structure with the graph that contains all
    stations since no colour is selected"""
    nodes_str_to_object = {}
    connections_node_neighbors = {}
    for tupla_data in file.items():
        node_name, node_data = tupla_data
        nodes_str_to_object[node_name] = Node(node_name, node_data["color"])
        connections_node_neighbors[node_name] = node_data["vecinos"]
    for tuple_node_stations in connections_node_neighbors.items():
        node_name, neighbors = tuple_node_stations
        for node in neighbors:
            if nodes_str_to_object[node] not in nodes_str_to_object[node_name].neighbors:
                nodes_str_to_object[node_name].add_neighbor(
                    nodes_str_to_object[node])
    return nodes_str_to_object
