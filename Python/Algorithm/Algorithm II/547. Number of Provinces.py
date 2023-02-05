def find_circle_num(is_connected: list[list[int]]) -> int:
    """
    Finding the total number of provinces in is_connected, and return it

    :param is_connected: Matrix of integers, represent connection between cities if [city][other_city] = 1, else 0
    :return: The total number of provinces in is_connected

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Integer counter for storing the amount of existing provinces
    provinces_counter = 0

    # Assisting function to make the DFS calls
    def map_provinces(city) -> None:
        """
        Recursive function for checking the current "city" (row) connections with other cities using DFS Algorithm

        :param city: Integer represent the current cell row, "city"
        :return: None, Everything happen in place
        """
        # Loop to traverse each city in is_connected and check if he is adjacent of the current city
        for other_city, adjacent in enumerate(is_connected[city]):

            # if the current city is connected to other city
            if adjacent:
                # Updating cell value from 1 to 0 for both connected cities, so we won't count them again
                is_connected[city][other_city] = 0
                is_connected[other_city][city] = 0

                # callback to the city of the current column, to map their connections to other cities
                map_provinces(other_city)

        # Return nothing, means we mapped the current city connection
        return

    # Loop to traverse every row in is_connected
    for row in range(len(is_connected)):

        # if we haven't checked the current city connections, then map its connections and update the provinces counter
        if is_connected[row][row]:
            map_provinces(row)
            provinces_counter += 1

    # Returning the amount of existing provinces
    return provinces_counter
