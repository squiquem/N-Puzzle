import sys
import copy
from goal import find_end

def error_exit(string):
    """
    Print + quit
    """
    print('Please enter correct', string)
    sys.exit(0)

def input_parsing(file):
    """
    Builds puzzle array from file
    """
    puzzle = []
    n = 0
    try:
        with open(file, 'r') as f:
            if f.mode == 'r':
                fl = f.readlines()
            else:
                error_exit('file')
            for x in fl:
                x = x.split('#')[0]
                if len(x.strip().split()) == 1:
                    try:
                        n = int(x)
                    except ValueError:
                        error_exit('n')
                if len(x.strip().split()) > 1:
                    puzzle.append(x.strip().split())
    except:
        error_exit("file")
    return n, puzzle

def error_checking(n, puzzle):
    """
    Verifying number of elements, elements value, doubles
    """
    l = []
    if len(puzzle) != n:
        return 1
    for i, p in enumerate(puzzle):
        if len(p) != n:
            return 1
        for j, x in enumerate(p):
            try:
                x = int(x)
            except ValueError:
                return 1
            if x >= n*n:
                return 1
            p[j] = x
            l.append(x)
        puzzle[i] = p
    if len(set([x for x in l if l.count(x) > 1])) > 0:
        return 1
    return 0

def zero_movement_parity(puzzle, n):
    """
    Finds the number of moves of 0 to reach final position
    """
    X, Y = find_end(0, n)
    h = abs(X - puzzle[0]['x']) 
    h += abs(Y - puzzle[0]['y'])
    return h%2

def resolution_parity(puzzle, n):
    """
    Finds the number of swaps between 2 pieces to reach final state
    """
    cpy = copy.deepcopy(puzzle)
    c = 0
    for k in sorted(puzzle.keys()):
        X, Y = find_end(k, n)
        if X == cpy[k]['x'] and Y == cpy[k]['y']:
            continue
        target = [k for k in cpy.keys() if cpy[k]['x'] == X and cpy[k]['y'] == Y]
        t = target[0]
        cpy[t]['x'], cpy[t]['y'] = cpy[k]['x'], cpy[k]['y']
        cpy[k]['x'], cpy[k]['y'] = X, Y
        c += 1
    return c%2

def is_solvable(puzzle, n):
    """
    If they have same parity, puzzle is solvable
    """
    if zero_movement_parity(puzzle, n) == resolution_parity(puzzle, n):
        print('Puzzle is SOLVABLE')
        return 1
    print('Puzzle is NOT SOLVABLE')
    return 0
