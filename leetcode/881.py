class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        boat = []
        cnt=0
        res=0
        for i in people:

            if limit > sum(boat):
            # 보트에 한명씩 태우기
                boat.append(i)
            # boat 출격    
            if limit == sum(boat):
                res+=1
                boat = []
            elif limit < sum(boat):
                boat = []
                res+=2
        if res==0:
            return 1
        else:
            return res
             
# tc 불합 다른 사람 풀이보니 two point 씀