from goal import find_end

def nb_coordinates(x, puzzle, n):
    """
    Finds coordinates of x in puzzle array
    """
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == x:
                return j, i

def get_row(i, array):
    """
    Gets column index of array
    """
    return array[i]

def get_col(j, array):
    """
    Gets row index of array
    """
    col = []
    for i in range(len(array)):
        col.append(array[i][j])
    return col

def manhattan_distance(u):
    """
    Calculates manhattan distance for puzzle array
    """
    h = 0
    for i in range(u.n):
        for j in range(u.n):
            tile = u.puzzle[i][j]

            # we may remove these 2 lines
            if tile == 0:
                continue

            col, row = find_end(tile, u.n)
            h += abs(row-i) + abs(col-j)
    return h

def hamming_distance(u):
    """
    Finds the nb of misplaced tiles
    """
    h = 0
    for i in range(u.n):
        for j in range(u.n):
            tile = u.puzzle[i][j]

            # we may remove these 2 lines
            if tile == 0:
                continue

            col, row = find_end(tile, u.n)
            if [i, j] != [col, row]:
                h += 1
    return h

def linear_conflict(u):
    """
    Two tiles tj and tk are in a linear conflict if tj and tk are on the same row,
    the goal positions of tj and tk are both in that row, tj is to the right of tk,
    and goal position of tj is on the left of the goal position of tk (for example).
    We do the same for columns.
    The linear conflict heuristic is calculated as Manhattan distance + 2*(Linear conflicts)
    """
    LC = 0
    for i in range(u.n):
        row = get_row(i, u.puzzle)
        for j in row:
            if j == 0:
                continue
            xj, yj = nb_coordinates(j, u.puzzle, u.n)
            Xj, Yj = find_end(j, u.n)
            others = [l for l in row if l not in [0, j]]
            for k in others:
                xk, yk = nb_coordinates(k, u.puzzle, u.n)
                Xk, Yk = find_end(k, u.n)
                if Yk == Yj and ((xk > xj and Xk < Xj) or (xk < xj and Xk > Xj)):
                    LC += 1
        col = get_col(i, u.puzzle)
        for j in col:
            if j == 0:
                continue
            xj, yj = nb_coordinates(j, u.puzzle, u.n)
            Xj, Yj = find_end(j, u.n)
            others = [l for l in col if l not in [0, j]]
            for k in others:
                xk, yk = nb_coordinates(k, u.puzzle, u.n)
                Xk, Yk = find_end(k, u.n)
                if Xk == Xj and ((yk > yj and Yk < Yj) or (yk < yj and Yk > Yj)):
                    LC += 1
    return LC + manhattan_distance(u)
