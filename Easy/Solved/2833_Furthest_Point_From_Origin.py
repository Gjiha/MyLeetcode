class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        position = 0
        underMove = 0
        for move in moves:
            if move == "L":
                position += 1
            elif move == "R":
                position -= 1
            else:
                underMove += 1
        
        tempTotal = abs(position) + underMove
        return tempTotal
        