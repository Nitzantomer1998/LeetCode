def tribonacci(n: int) -> int:
    
    tri = [0, 1, 1]

    for _ in range(n - 2):
        tri[0], tri[1], tri[2] = tri[1], tri[2], sum(tri)

    return tri[n] if n < 3 else tri[-1]
