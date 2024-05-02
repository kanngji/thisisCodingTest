# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lt = 1
        rt = n

        while (lt<rt):
            middle = (lt+rt)//2
            if isBadVersion(middle)==True:
                rt=middle
            else:
                lt=middle+1
        return lt