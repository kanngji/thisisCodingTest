import itertools

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        arr = [i for i in range(1,k+1)]
        permutations = itertools.product(arr,repeat=n)

        cnt = 0

        for combo in permutations:
            if sum(combo)==target:
                cnt+=1

        return cnt 


# timelimit
    
