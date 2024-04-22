class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        if '0000' in visited:
            return -1
            
        stepsCounter = 0
        deque = collections.deque(['0000'])
        while deque:
            currentLevel = len(deque)

            for _ in range(currentLevel):
                currentLock = deque.popleft()

                if currentLock == target:
                    return stepsCounter

                for index in range(4):
                    digit = int(currentLock[index])
                    for dir in [-1, 1]:
                        newDigit = (digit + dir) % 10
                        nextLock = currentLock[:index] + str(newDigit) + currentLock[index + 1:]

                        if nextLock not in visited:
                            deque.append(nextLock)
                            visited.add(nextLock)
                            
            stepsCounter += 1
        return -1
