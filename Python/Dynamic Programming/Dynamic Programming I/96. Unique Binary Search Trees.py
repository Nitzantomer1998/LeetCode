def num_trees(n: int) -> int:
   
    catalan = 1
    for i in range(n):
        catalan *= 2 * (2 * i + 1)
        catalan //= (i + 2)

    return catalan
