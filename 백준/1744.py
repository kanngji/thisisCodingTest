from queue import PriorityQueue
n = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one = 0
zero = 0

for i in range(n): # 4가지로 데이터분리 저장
    data = int(input())
    if data > 1:
        plusPq.put(data * -1) # 양수 내림차순 정렬을 위해 -1를 곱하여 저장 낮은수가 높은 우선순위
    elif data == 1:
        one += 1 # 1의 개수 추가
    elif data == 0:
        zero +=1 # 0의 개수 추가
    else:
        minusPq.put(data)

sum = 0

while plusPq.qsize() > 1: # 양수 처리
    first = plusPq.get() * -1
    second = plusPq.get() * -1
    sum += first * second

if plusPq.qsize() > 0:
    sum += plusPq.get()* -1 # plusPq가 한개일때 그 한개 더하기

while minusPq.qsize() > 1: # 음수 처리
    first = minusPq.get()
    second = minusPq.get()
    sum += first * second

if minusPq.qsize() > 0:
    if zero ==0:
        sum+=minusPq.get()
        
sum+=one
print(sum)