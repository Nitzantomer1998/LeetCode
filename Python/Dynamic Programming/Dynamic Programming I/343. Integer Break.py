def integer_break(n: int) -> int:
    
    MP = [value for value in range(n + 1)]
    MP[-1] = 0

    for number in range(2, n + 1):
        for index in range(1, number):
            MP[number] = max(MP[number], MP[index] * MP[number - index])

    return MP[-1]
