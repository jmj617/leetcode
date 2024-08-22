class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        first = 0
        for i in range(len(commands)):
            if commands[i] == "RIGHT":
                first += 1
            elif commands[i] == "DOWN":
                first += n
            elif commands[i] == "UP":
                first -= n
            elif commands[i] == "LEFT":
                first -= 1
        return first
                