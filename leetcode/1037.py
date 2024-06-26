class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 기울기가 같아야한다.
        (x1,y1) , (x2,y2) , (x3,y3) = points

        return (y2-y1) * (x3 -x2) != (y3-y2) * (x2-x1)