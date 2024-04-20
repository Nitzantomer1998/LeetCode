class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def FindFarmlandCoordinates(startRow: int, startColumn: int) -> List[int]:
            coordinates = [startRow, startColumn]
            endRow = startRow
            endColumn = startColumn
            
            while endRow < rows and land[endRow][startColumn]:
                endRow += 1
            
            while endColumn < columns and land[startRow][endColumn]:
                endColumn += 1
            
            for row in range(startRow, endRow):
                for column in range(startColumn, endColumn):
                    land[row][column] = 0

            coordinates.extend([endRow - 1, endColumn - 1])
            return coordinates

        farmlands = []
        rows = len(land)
        columns = len(land[0])
        
        for row in range(rows):
            for column in range(columns):
                if land[row][column]:
                    farmland = FindFarmlandCoordinates(row, column)
                    farmlands.append(farmland)
        
        return farmlands
