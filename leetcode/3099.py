class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x=str(x)
        divisible=sum(int(i)for i in x)
        if int(x)%divisible==0:
            return divisible
        else:
            return -1