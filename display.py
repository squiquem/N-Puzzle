def print_info(u, c=None):
    """
    Prints evolution
    """
    if c:
        print('c=', c, end=' ')
    print('f=', u.f, 'g=', u.g)
    print('Puzzle:')
    print(u)
    print('')
    return

def rebuild_path(u):
    """
    Builds path from start to solution
    """
    lst = [u]
    print('REBUILD PATH')
    while u.parent:
        lst.insert(0, u.parent)
        u = u.parent
        
    print('Nb of moves:', len(lst)-1)
    for elmt in lst:
        print_info(elmt)
    return

def print_solution(u, c, L, P):
    """
    Prints solution
    """
    print('END:')
    print_info(u, c)
    rebuild_path(u)
    print('Time complexity (opened set size):', L)
    print('Size complexity (priority queue max size):', P)
    print('Nb of nodes explored:', c)
    return
