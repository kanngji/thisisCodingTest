class Solution:
    def isPathCrossing(self, path: str) -> bool:
        

        stand = (0,0)
        se = set()
        se.add((0,0))
        y,x=0,0
        for i in path:

            
            if i == 'N':
                y+=1
            elif i == "E":
                x+=1
            elif i == "S":
                y-=1
            elif i == "W":
                x-=1
            
            if (y,x) in se:
                return True
            se.add((y,x))
        return False
        