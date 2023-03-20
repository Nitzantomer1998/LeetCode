def num_squares(n: int) -> int:
    
    squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

    counts = [n + 1] * (n + 1)

    counts[0] = 0

    for i in range(1, n + 1):

        for square in squares:

            if square > i:
                break

            counts[i] = min(counts[i], counts[i - square] + 1)

    return counts[n]
