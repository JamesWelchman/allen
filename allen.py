from itertools import product
from collections import namedtuple
from functools import reduce
from queue import Queue


from composition import BASIC_COMPOSITION

RelationPair = namedtuple("RelationPair", (
    "name0",
    "relation",
    "name1",
))


class Relation:
    """
    Relation wraps a set representing a set of basic relations
    """
    def __init__(self, basic_relations):
        self._basic_relations = basic_relations

    def compose(self, other):
        ans = set()
        for (r1, r2) in product(self._basic_relations, other._basic_relations):
            ans.update(basic_compose(r1, r2))

        return Relation(ans)

    def intersection(self, other):
        return Relation(self._basic_relations.intersection(other._basic_relations))

    def __add__(self, other):
        return self.compose(other)


def basic_compose(r1, r2):
    """
    basic_compose will take two relations
    (both represented as characters) and
    return a set representing the basic composition.
    """

    return BASIC_COMPOSITION[(r1, r2)]


class DirectedGraph:
    """
    Graph represents a directed acyclic graph of allen relations
    relations.
    """
    def __init__(self, relations):
        """
        relations should be a list of RelationPair instances
        """

        self._relations = relations
        self._adj = {}
        self._edges = {}

        # Build adj
        for r in relations:
            ll = self._adj.get(r.name0) or []
            ll.append(r.name1)
            self._adj[r.name0] = ll

        # edges is a map (v1, v2) -> relation
        for (n1, r, n2) in relations:
            self._edges[(n1, n2)] = r

    def compute_relation(self, name1, name2):
        assert name1 in self._adj, "start vertex is invalid"

        return reduce(lambda x, y: x.intersection(y), self._relation_path_gen(name1, name2))

    def _relation_path_gen(self, name1, name2):
        for path in breadth_first_search(self._adj, name1, name2):
            relation = self._edges[(path[0], path[1])]

            # consume the vertex names in pairs
            for i in range(1, len(path) - 1):
                n1 = path[i]
                n2 = path[i + 1]
                r = self._edges[(n1, n2)]
                relation = relation + r

            yield relation


def breadth_first_search(nodes, start_node, end_node):
    yield from _breadth_first_search(nodes, [start_node], set([start_node]), end_node)


def _breadth_first_search(nodes, path, visited, end_node):
    """
    breadth_first_search will find all paths
    """

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
            yield from _breadth_first_search(nodes, new_path, new_visited, end_node)
