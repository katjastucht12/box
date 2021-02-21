import networkx as nx
import pytest

from search import NodeDoesNotExist, search, nodes, edges

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)


def test_non_existing_start():
    with pytest.raises(NodeDoesNotExist):
        search("XXX", "DUB", G)


def test_non_existing_end():
    with pytest.raises(NodeDoesNotExist):
        search("DUB", "XXX", G)


def test_non_string():
    with pytest.raises(NodeDoesNotExist):
        search("DUB", 1, G)


def test_same_locations():
    result, result_string, total_time = search("DUB", "DUB", G)
    assert total_time is 0
    assert len(result) is 0


def test_path_does_not_exist():
    edges2 = [('DUB', 'CDG', 2), ('CDG', 'BOS', 6), ('CDG', 'BKK', 6),
              ('ORD', 'LAS', 2), ('NYC', 'LAS', 3), ('BOS', 'LAX', 4),
              ('BKK', 'SYD', 11), ('LAX', 'LAS', 2), ('DUB', 'ORD', 6),
              ('LAX', 'SYD', 13), ('LAS', 'SYD', 14)
              ]
    nodes2 = ['DUB', 'LHR', 'CDG', 'BOS', 'BKK', 'ORD', 'LAS',
              'NYC', 'LAS', 'BOS', 'LAX', 'SYD', ]

    G2 = nx.Graph()
    G2.add_nodes_from(nodes2)
    G2.add_weighted_edges_from(edges2)

    with pytest.raises(nx.NetworkXNoPath):
        search("DUB", "LHR", G2)


def test_returns_correct_return_format():
    result, result_string, total_time = search("DUB", "SYD", G)
    assert total_time is 21
    assert len(result) is 3
    assert result[0][0] is 'DUB'
    assert result[0][1] is 'LHR'
    assert result[1][0] is 'LHR'
    assert result[1][1] is 'BKK'
    assert result[2][0] is 'BKK'
    assert result[2][1] is 'SYD'
