def single_number(numbers: list[int]) -> int:
    
    single_number_solution = 0

    for value in numbers:
        
        single_number_solution ^= value

    return single_number_solution
