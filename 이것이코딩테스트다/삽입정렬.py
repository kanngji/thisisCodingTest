# '데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입하면 어떨까? ' 
array = [7,5,9,0,0,2,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i 부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한칸 씩 왼쪽으로 이동 뒤에것이 앞에꺼보다 작으면
            array[j],array[j-1] = array[j-1],array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

# range의 세 번째 매개 변수
# range의 매개 변수 3개 (start , end ,step)이다
# 세 번째 매개 변수인 step에 -1이 들어가면 start 인덱스부터 시작해서 end + 1
# 인덱스까지 1씩 감소한다. 앞의 코드에서는 j변수가 i 부터 1까지 1씩 감소한다


