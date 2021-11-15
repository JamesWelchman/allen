from itertools import product
from collections import namedtuple
from functools import reduce

from composition import BASIC_COMPOSITION

# VertexPair represents two verticies and
# an edge. The edge, named relation must
# implement the + operator.
VertexPair = namedtuple("VertexPair", (
    "name0",
    "relation",
    "name1",
))


class Relation:
    """
    Relation wraps a set representing a set of basic relations
    """
    def __init__(self, basic_relations):
        """
        basic_relations is a set of characters
        (e.g) {'f', 'e', 'F'}
        """
        self._basic_relations = basic_relations

    def compose(self, other):
        """
        allen algebra compose operation
        """
        ans = set()
        for (r1, r2) in product(self._basic_relations, other._basic_relations):
            ans.update(basic_compose(r1, r2))

        return Relation(ans)

    def intersection(self, other):
        return Relation(self._basic_relations.intersection(other._basic_relations))

    def __add__(self, other):
        """
        we overload + as compose for use in the graph below
        """
        return self.compose(other)


def basic_compose(r1, r2):
    """
    basic_compose will take two basic relations
    (both represented as characters) and
    return a set representing the basic composition.
    """

    return BASIC_COMPOSITION[(r1, r2)]


class DirectedGraph:
    """
    Graph represents a directed (possibly cyclic) graph
    """
    def __init__(self, relations):
        """
        relations should be a list of VertexPair instances.
        """
        self._adj = {}
        self._edges = {}

        # Build adj
        # adj is a map from vertex names to a list of connected vertex
        # {"vertex_one": ["vertex_two", "vertex_three"], .. }
        for r in relations:
            ll = self._adj.get(r.name0) or []
            ll.append(r.name1)
            self._adj[r.name0] = ll

        # edges is a map from vertex pairs to relations
        # {("vertex_one", "vertex_two"): edge1, ...}
        for (n1, r, n2) in relations:
            self._edges[(n1, n2)] = r

    def compute_relation(self, name1, name2):
        assert name1 in self._adj, "start vertex is invalid"

        # We find all possible relations between name1 and name2 and compute
        # the intersection on these sets - giving our final answer.
        return reduce(lambda x, y: x.intersection(y), self._relation_path_gen(name1, name2))

    def _relation_path_gen(self, name1, name2):
        """
        _relation_path_gen is a generator yielding all relations
        between name1 and name2
        e.g (between "vertex_name1" and "vertex_name2")
        """
        for path in graph_traverse(self._adj, name1, name2):
            # path is a tuple of vertex names ("vertex_one", "vertex_two")
            # we want to examine our edges and compute a single relation
            # for a weighted graph this is the sum
            # for an allen graph, this is a repeated composition operation.
            relation = self._edges[(path[0], path[1])]

            # consume the vertex names in pairs
            for i in range(1, len(path) - 1):
                n1 = path[i]
                n2 = path[i + 1]
                r = self._edges[(n1, n2)]
                relation = relation + r

            yield relation


def graph_traverse(nodes, start_node, end_node):
    """
    graph_traverse will find all paths from start_node to end_node
    nodes is a map from node names to a list of adjacent nodes

    e.g
    nodes = {
        "one": ["two", "three"],
        "two": ["three"],
    }
    graph_traverse(nodes, "one", "three")
    ["one", "three"],
    ["one", "two", "three"]
    """
    yield from _graph_traverse(nodes, [start_node], set([start_node]), end_node)


def _graph_traverse(nodes, path, visited, end_node):
    current = path[-1]

    for neighbour in nodes.get(current, []):
        if neighbour in visited:
            continue

        new_path = path + [neighbour]

        if neighbour == end_node:
            yield tuple(new_path)
        else:
            new_visited = visited.copy()
            new_visited.add(neighbour)
            yield from _graph_traverse(nodes, new_path, new_visited, end_node)
