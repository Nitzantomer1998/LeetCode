def is_happy(n: int) -> bool:
    
    seen = set()

    while n != 1 and n not in seen:

        seen.add(n)

        current_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)

            current_sum += digit ** 2

        n = current_sum

    return n == 1
