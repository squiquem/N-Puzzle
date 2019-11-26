def find_edge(q, n):
    """
    Find the final position from value: side number and position on this side
    With n=4:
    1,2,3,4 are side 1
    5,6,7 -> 2
    8,9,10 -> 3
    11,12 -> 4
    13,14 -> 5
    15 -> 6
    """
    e = 1
    if q == 0:
        q = n * n
    while q > n:
        q -= n
        if e % 2 == 1:
            n -= 1
        e += 1
    return e, q - 1

def xy_from_edge(e, q, n):
    """
    Find position from side number parameter and position on this side
    """
    if e % 4 == 1:
        x, y = q + e // 4, e // 4
    elif e % 4 == 2:
        x, y = n - 1 - e // 4, q + 1 + e // 4
    elif e % 4 == 3:
        x, y = n - 2 - q - e // 4, n - 1 - e // 4
    else:
        x, y = e // 4 - 1, n - 1 - e // 4 - q
    return x, y

def find_end(m, n):
    """
    Finds final position of m in snail solution
    """
    e, q = find_edge(m, n)
    return xy_from_edge(e, q, n)
