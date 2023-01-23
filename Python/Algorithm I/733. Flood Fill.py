def flood_fill(image: list[list[int]], start_row: int, start_column: int, color: int) -> list[list[int]]:
    """
    Modify image, with the starting indices and the sent color change every cell in the 4 directions with the same color

    :param image: Matrix of integers, represent a picture
    :param start_row: Integer of the starting row
    :param start_column: Integer of the starting column
    :param color: Integer represent the new modify color
    :return: The image after it been updated

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Constants for the cells indices boundaries, for more readable code
    MAX_ROW = len(image)
    MAX_COLUMN = len(image[0])

    # Storing the first color before painting
    old_color = image[start_row][start_column]

    # Assisting function to make the DFS calls
    def fill(row: int, column: int) -> None:
        """
        Recursive function for updating / filing the needed image cells using DFS Algorithm

        :param row: Integer represent the current cell row
        :param column: Integer represent the current cell column
        :return: None, Everything happen in place
        """
        # if the sent indices are invalid, return
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN):
            return

        # if the current cell cant be painted or already painted, return
        if image[row][column] != old_color or image[row][column] == color:
            return

        # Update the cell color
        image[row][column] = color

        # callback to the other 4 directions for a possible color
        fill(row - 1, column)
        fill(row + 1, column)
        fill(row, column - 1)
        fill(row, column + 1)

    # Activating the fill recursion
    fill(start_row, start_column)

    # Returning the modified image
    return image
