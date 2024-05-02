from collections import deque
class Solution:
    def splitNum(self, num: int) -> int:
        num = str(num)
        num1=""
        num2=""

        num = sorted(num)
        numarr = deque(num)

        for i in range(len(num)):
            if i%2==0:
                num1+=numarr.popleft()
            else:
                num2+=numarr.popleft()

        return int(num1)+int(num2)