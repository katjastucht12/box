import networkx as nx
import matplotlib.pyplot as plt
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

edges = [('DUB', 'LHR', 1), ('DUB', 'CDG', 2),
         ('CDG', 'BOS', 6), ('CDG', 'BKK', 6),
         ('ORD', 'LAS', 2), ('LHR', 'NYC', 5),
         ('NYC', 'LAS', 3), ('BOS', 'LAX', 4),
         ('LHR', 'BKK', 9), ('BKK', 'SYD', 11),
         ('LAX', 'LAS', 2), ('DUB', 'ORD', 6),
         ('LAX', 'SYD', 13), ('LAS', 'SYD', 14)
         ]
nodes = ['DUB', 'LHR', 'CDG', 'BOS', 'BKK', 'ORD', 'LAS',
         'NYC', 'LAS', 'BOS', 'LAX', 'SYD', ]


class NodeDoesNotExist(Exception):
    def __init__(self, message="Node Does not exist"):
        super().__init__(message)


def search(start, end, G):
    if start not in nodes:
        raise NodeDoesNotExist(message=f' {start} does not exist')
    elif end not in nodes:
        raise NodeDoesNotExist(message=f' {end} does not exist')
    else:
        logging.info(f'finding path from {start} to {end}')
        path = nx.dijkstra_path(G, start, end, weight='cost')
        pairs = zip(path, path[1:])
        total = 0
        result_str = ""
        res = []
        for pair in pairs:
            weight = G.get_edge_data(pair[0], pair[1])['weight']
            total += weight
            result_str += f'{pair[0]} -- {pair[1]} ({weight}) \n'
            res.append((pair[0], pair[1], weight))
        result_str += f'time: {total}'
        return res, result_str, total


if __name__ == "__main__":
    start = sys.argv[1]
    end = sys.argv[2]
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    try:
        result, result_string, total_time = search(start, end, G)
        logging.info(f'path found : \n{result_string}')
    except nx.NetworkXNoPath:
        logging.error(f' No path exists between {start} and {end}')
    except NodeDoesNotExist as e:
        logging.error(str(e))

# pos = nx.spring_layout(G)
#     labels = nx.get_edge_attributes(G,'weight')
#     nx.draw_networkx(G,pos,node_color='green', node_size =700, with_labels = True, alpha=0.7)
#     nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#     plt.show()
