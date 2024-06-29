class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        n = num // 2

        for i in range(1,n+1):
            if i * i == num:
                return True
        return False


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left , right = 1 , num

        while left <= right:
            mid = left + (right -left) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False