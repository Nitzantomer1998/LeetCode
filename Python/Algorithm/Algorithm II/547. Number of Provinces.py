def find_circle_num(is_connected: list[list[int]]) -> int:
    
    provinces_counter = 0

    def map_provinces(city) -> None:
        
        for other_city, adjacent in enumerate(is_connected[city]):

            if adjacent:
                is_connected[city][other_city] = 0
                is_connected[other_city][city] = 0

                map_provinces(other_city)

        return

    for row in range(len(is_connected)):

        if is_connected[row][row]:
            map_provinces(row)
            provinces_counter += 1

    return provinces_counter
