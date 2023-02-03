def backspace_compare(s: str, t: str) -> bool:
    
    i = len(s) - 1
    j = len(t) - 1

    counter_s = 0
    counter_t = 0

    while i >= 0 or j >= 0:


        while i >= 0 and (counter_s > 0 or s[i] == '#'):

            if s[i] == '#':
                counter_s += 1

            else:
                counter_s -= 1

            i -= 1

        while j >= 0 and (counter_t > 0 or t[j] == '#'):

            if t[j] == '#':
                counter_t += 1

            else:
                counter_t -= 1

            j -= 1

        s_current_char = None if i < 0 else s[i]
        t_current_char = None if j < 0 else t[j]

        if s_current_char != t_current_char:
            return False

        i -= 1
        j -= 1

    return True
