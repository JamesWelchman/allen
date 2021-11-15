from allen import graph_traverse, VertexPair, DirectedGraph


def test_graph_traverse_first_search_single():
    nodes = {
        "one": ["two", "three"],
    }

    assert set(graph_traverse(nodes, "one", "two")) == set([("one", "two")])
    assert set(graph_traverse(nodes, "one", "three")) == set([("one", "three")])
    assert not set(graph_traverse(nodes, "two", "three"))


def test_graph_traverse_first_search_double():
    nodes = {
        "one": ["two", "three"],
        "two": ["three"],
    }

    assert set(graph_traverse(nodes, "one", "three")) == {("one", "three"), ("one", "two", "three")}
    assert set(graph_traverse(nodes, "one", "two")) == set([("one", "two")])
    assert set(graph_traverse(nodes, "two", "three")) == set([("two", "three")])
    assert not set(graph_traverse(nodes, "three", "two"))


def test_graph_traverse_first_double_triple():
    nodes = {
        "one": ["two", "three", "four"],
        "two": ["three", "four"],
        "three": ["one", "four"],
        "four": ["two"],
    }

    assert set(graph_traverse(nodes, "one", "two")) == {("one", "two"), ("one", "four", "two"), ("one", "three", "four", "two")}
    assert set(graph_traverse(nodes, "one", "three")) == {("one", "three"),
                                                               ("one", "two", "three"),
                                                               ("one", "four", "two", "three")}
    assert set(graph_traverse(nodes, "one", "four")) == {("one", "four"),
                                                               ("one", "two", "four"),
                                                               ("one", "three", "four"),
                                                               ("one", "two", "three", "four")}
    assert set(graph_traverse(nodes, "two", "one")) == set([("two", "three", "one")])
    assert set(graph_traverse(nodes, "two", "three")) == set([("two", "three")])
    assert set(graph_traverse(nodes, "two", "four")) == {("two", "four"),
                                                               ("two", "three", "four"),
                                                               ("two", "three", "one", "four")}
    assert set(graph_traverse(nodes, "three", "one")) == set([("three", "one")])
    assert set(graph_traverse(nodes, "three", "two")) == {("three", "one", "two"),
                                                                ("three", "one", "four", "two"),
                                                                ("three", "four", "two")}
    assert set(graph_traverse(nodes, "three", "four")) == {("three", "four"),
                                                                 ("three", "one", "four"),
                                                                 ("three", "one", "two", "four")}
    assert set(graph_traverse(nodes, "four", "one")) == set([("four", "two", "three", "one")])
    assert set(graph_traverse(nodes, "four", "two")) == set([("four", "two")])
    assert set(graph_traverse(nodes, "four", "three")) == set([("four", "two", "three")])


class Relation:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Relation(self.x + other.x)

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return hash(self.x)


def test_dgraph_relation_one():
    edges = [
        VertexPair("one", Relation(3), "two"),
    ]

    assert list(DirectedGraph(edges)._relation_path_gen("one", "two")) == [Relation(3)]


def test_dgraph_relation_two():
    edges = [
        VertexPair("one", Relation(7), "two"),
        VertexPair("one", Relation(11), "three"),
        VertexPair("two", Relation(13), "three"),
    ]

    dgraph = DirectedGraph(edges)

    assert list(dgraph._relation_path_gen("one", "two")) == [Relation(7)]
    assert set(dgraph._relation_path_gen("one", "three")) == {Relation(20), Relation(11)}
    assert list(dgraph._relation_path_gen("two", "three")) == [Relation(13)]
    assert not list(dgraph._relation_path_gen("two", "one"))
    assert not list(dgraph._relation_path_gen("three", "one"))
    assert not list(dgraph._relation_path_gen("three", "two"))


def test_graph_relation_three():
    edges = [
        VertexPair("one", Relation(7), "two"),
        VertexPair("one", Relation(11), "three"),
        VertexPair("one", Relation(13), "four"),
        VertexPair("two", Relation(19), "three"),
        VertexPair("three", Relation(23), "one"),
        VertexPair("three", Relation(29), "four"),
        VertexPair("four", Relation(31), "two"),
    ]

    dgraph = DirectedGraph(edges)

    assert set(dgraph._relation_path_gen("one", "two")) == {Relation(7), Relation(13 + 31), Relation(11 + 29 + 31)}
    assert set(dgraph._relation_path_gen("one", "three")) == {Relation(11),
                                                              Relation(7 + 19),
                                                              Relation(13 + 31 + 19)}
    assert set(dgraph._relation_path_gen("one", "four")) == {Relation(13),
                                                             Relation(11 + 29),
                                                             Relation(7 + 19 + 29)}
    assert list(dgraph._relation_path_gen("two", "one")) == [Relation(19 + 23)]
    assert list(dgraph._relation_path_gen("two", "three")) == [Relation(19)]
    assert set(dgraph._relation_path_gen("two", "four")) == {Relation(19 + 29), Relation(19 + 23 + 13)}
    assert list(dgraph._relation_path_gen("three", "one")) == [Relation(23)]
    assert set(dgraph._relation_path_gen("three", "two")) == {Relation(23 + 7),
                                                              Relation(23 + 13 + 31),
                                                              Relation(29 + 31)}
    assert set(dgraph._relation_path_gen("three", "four")) == {Relation(29),
                                                               Relation(23 + 13)}
    assert list(dgraph._relation_path_gen("four", "one")) == [Relation(31 + 19 + 23)]
    assert list(dgraph._relation_path_gen("four", "two")) == [Relation(31)]
    assert list(dgraph._relation_path_gen("four", "three")) == [Relation(31 + 19)]
