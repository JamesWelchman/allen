
from allen import basic_compose, Relation
from composition import FULL

def test_basic_comp():
    assert basic_compose('p', 'p') == 'p'
    assert basic_compose('p', 'P') == FULL

    assert basic_compose('o', 'o') == 'pmo'
    assert basic_compose('o', 'f') == 'osd'
    assert basic_compose('o', 'd') == 'pmosd'

    # not symmetric
    assert basic_compose('O', 'S') == 'O'
    assert basic_compose('S', 'O') == 'OMP'


def test_relation_compose_single():
    r1 = Relation({"o"})
    r2 = Relation({"o", "f", "d"})

    assert r1.compose(r2)._basic_relations == {"p", "m", "o", "s", "d"}


def test_relation_compose_double():
    r1 = Relation({"o", "F", "D"})
    r2 = Relation({"o", "F", "D", "s", "e", "S"})

    assert r1.compose(r2)._basic_relations == {"p", "m", "o", "F", "D"}


def test_intersection():
    r1 = Relation({"o", "F", "D"})
    r2 = Relation({"o", "F", "D", "s", "e", "S"})

    assert r1.intersection(r2)._basic_relations == {"o", "F", "D"}
    
