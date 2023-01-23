def flood_fill(image: list[list[int]], start_row: int, start_column: int, color: int) -> list[list[int]]:
    
    MAX_ROW = len(image)
    MAX_COLUMN = len(image[0])

    old_color = image[start_row][start_column]

    def fill(row: int, column: int) -> None:
        
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN):
            return

        if image[row][column] != old_color or image[row][column] == color:
            return

        image[row][column] = color

        fill(row - 1, column)
        fill(row + 1, column)
        fill(row, column - 1)
        fill(row, column + 1)

    fill(start_row, start_column)

    return image
