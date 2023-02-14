def num_decodings(string: str) -> int:
   
    if string[0] == '0':
        return 0

    nth_decodings_counter = [0 for _ in range(len(string) + 1)]

    nth_decodings_counter[0] = nth_decodings_counter[1] = 1

    for index in range(2, len(string) + 1):

        if string[index - 1] != '0':
            nth_decodings_counter[index] = nth_decodings_counter[index - 1]

        if 10 <= int(string[index - 2: index]) <= 26:
            nth_decodings_counter[index] += nth_decodings_counter[index - 2]

    return nth_decodings_counter[-1]
