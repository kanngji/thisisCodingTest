class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        if num == 0:
            return True
        num_str = str(num)

        if num_str[-1]=='0':
            return False

        return True