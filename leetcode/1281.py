class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        product=1
        sum=0
        for i in n:
            i=int(i)
            product=product*i
            sum=sum+i
        return product-sum