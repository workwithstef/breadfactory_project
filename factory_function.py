
def make_dough(ingredient1, ingredient2):
    if ingredient1 == 'water' and ingredient2 == 'flour':
        return 'dough'
    elif ingredient1 == 'flour' and ingredient2 == 'water':
        return 'dough'
    else:
        return 'not dough'


oven = make_dough('water', 'flour')


def bake_bread(oven):
    if oven == 'dough':
        return 'bread'
    else:
        return 'not bread'


def wholewheat_dough(ingredient1, ingredient2):
    if ingredient1 == 'water' and ingredient2 == 'wholewheat flour':
        return 'wholewheat dough'
    elif ingredient1 == 'wholewheat flour' and ingredient2 == 'water':
        return 'wholewheat dough'
    else:
        return 'not wholewheat dough'


whole_oven = wholewheat_dough('water', 'wholewheat flour')


def wholewheat_bread(whole_oven):
    if whole_oven == 'wholewheat dough':
        return 'wholewheat bread'
    else:
        return 'not wholewheat bread'
