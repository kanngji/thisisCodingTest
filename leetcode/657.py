class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = [0,0]
        for i in moves:
            if i == 'U':
                direction[0]+=1
            elif i == 'D':
                direction[0]-=1
            elif i == "R":
                direction[1]+=1
            elif i == "L":
                direction[1]-=1
            
        return direction == [0,0]