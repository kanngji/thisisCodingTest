# 야근지수


def solution(n, works):
    answer = 0
    while n!=0:
        works.sort(reverse=True)
        if (works[0])==0:
            break
        works[0]=works[0]-1
        n-=1
        
    for i in works:
        answer+=i**2
        
    return answer

# 효율성 검사 실패 ㅠㅠ sort 말고 heap써야함

import heapq

def solution(n,works):
    if n>=sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        i = heapq.heappop(works)
        i+=1
        heapq.heappush(works,i)

    return sum([w**2 for w in works])