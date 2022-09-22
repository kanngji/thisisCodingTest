# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까? 

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        #피벗 보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left]<=array[pivot]:
            left+=1
        #피벗 보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right]>=array[pivot]:
            right-=1
        
        if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        
#분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

#####################################################################
#파이썬의 장점을 살려 짧게 작성한 퀵 정렬 소스 코드

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side)+ [pivot] + quick_sort(right_side)

print(quick_sort(array))