# [1차] 캐시

from collections import deque
cities=	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
arr=deque()
cities=deque(cities)
answer=0 # 총 실행시간


while len(cities)!=0:
  
  if cities[0] not in arr: # cache miss
    arr.append(cities.popleft()) 
    answer+=5
  elif cities[0] in arr: # cache hit
    a=cities.popleft()
    arr.remove(a)
    arr.appendleft(a)
    answer+=1

  

print(answer)
      
    
  
### 캐시크기를 조절하는 방법에서 막혀서 다른사람 풀이봄

def solution(cacheSize, cities):
    answer = 0
    cache=[]
    # 캐시가 없을 경우
    if cacheSize==0: return len(cities)*5
    
    for city in cities:
        # cache hit
        if city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower()) # 해당 도시를 리스트의 맽 뒤로
            answer+=1
        # cache miss
        else:
            if len(cache)==cacheSize: cache.pop(0)
            cache.append(city.lower())
            answer+=5
    return answer