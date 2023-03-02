def get_max_len(numbers: list[int]) -> int:
    
    max_length = positive = negative = 0

    for number in numbers:

        if number == 0:
            positive = negative = 0

        elif number > 0:
            positive += 1

            negative = 0 if negative == 0 else negative + 1

        else:
            positive, negative = 0 if negative == 0 else negative + 1, positive + 1

        max_length = max(max_length, positive)

    return max_length
