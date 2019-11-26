import queue
from parse import is_solvable, error_exit, error_checking, input_parsing
from display import print_solution, print_info

class Node:
    def __init__(self, array, n, zero, parent=None, bonus=None):
        """
        Node definition
        """
        self.n = n
        self.puzzle = array
        self.zero = zero
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = parent if parent else None
        self.bonus = bonus
        
    def __lt__(self, other):
        if self.bonus == 'ucs':
            return (self.h < other.h) if self.g == other.g else (self.g < other.g)
        elif self.bonus == 'greedy':
            return (self.g < other.g) if self.h == other.h else (self.h < other.h)
        else:
            return (self.h < other.h) if self.f == other.f else (self.f < other.f)
    
    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __repr__(self):
        return str(self.puzzle)
    
    def __str__(self):
        string = ''
        for i in range(self.n):
            for j in range(self.n):
                x = str(self.puzzle[i][j])
                string += '{0:2} '.format(x)
            if i < self.n-1:
                string += '\n'
        return string
    
    def __hash__(self):
        return hash(tuple([tuple(i) for i in self.puzzle]))

def puzzle_structure(n, puzzle):
    """
    Builds nested dictionary from puzzle array values
    """
    dpuz = {}
    for i, p in enumerate(puzzle):
        for j, m in enumerate(p):
            dpuz[m] = {
                'x' : j,
                'y' : i,
            }
    return dpuz

def find_neighb_from_array(u, variant, bonus, heuristic):
    """
    Finds neighbors nodes
    Creates a list of them
    """
    neighbors = []
    move = {
        'up' : [-1,0],
        'down' : [1,0],
        'right' : [0,1],
        'left' : [0,-1]
    }
    for k,v in move.items():
        cpy = [x[:] for x in u.puzzle]
        Y, X = u.zero['y'] + v[0], u.zero['x'] + v[1]
        if 0 <= X <= u.n - 1 and 0 <= Y <= u.n - 1:
            cpy[u.zero['y']][u.zero['x']], cpy[Y][X] = cpy[Y][X], 0
            new = Node(cpy, u.n, dict(x=X, y=Y), parent=u, bonus=bonus)
            new.g = u.g + 1
            new.h = variant * heuristic(new)
            new.f = new.g + new.h
            neighbors.append(new)
    return neighbors

def algo(start, variant, bonus, heuristic):
    """
    A* algorithm
    """
    n = start.n
    pq = queue.PriorityQueue()
    pq.put(start)
    open_set= { start : 0 }
    c, M = 0, 0
    print("Nb of config tested:")
    while not pq.empty():
        c+=1
        M = max(len(pq.queue), M)
        u = pq.get()

        # debug
        if c % 10000 == 0:
            print('{:,}'.format(c).replace(',', ' '))

        if u.h == 0:
            print_solution(u, c, len(open_set), M)
            return 1
        neighbors_list = find_neighb_from_array(u, variant, bonus, heuristic)
        for v in neighbors_list:
            if v not in open_set or open_set[v] > v.g:
                pq.put(v)
                open_set[v] = v.g
    return 0

def solve_puzzle(file, variant, bonus, heuristic):
    """
    Parsing + resolution
    """
    if bonus and bonus not in ['greedy', 'ucs']:
        error_exit('bonus')
    n, puz = input_parsing(file)
    if error_checking(n, puz):
        error_exit('puzzle')
    dpuz = puzzle_structure(n, puz)
    if is_solvable(dpuz, n):
        start = Node(puz, n, dpuz[0], bonus=bonus)
        start.f = start.h = heuristic(start)
        print('START:')
        print_info(start)
        print('')
        result = 'WIN' if algo(start, variant, bonus, heuristic) else 'LOSE'
        print(result)
    return
