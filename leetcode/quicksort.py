def quicksort(arr):
  if len(arr) <= 1:
    return arr

  else:
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    
    mid = [x for x in arr if x == pivot]
    
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)

arr = [3,6,8,10,1,2]
sorted_arr = quicksort(arr)
print(sorted_arr)

# 리스트 중  하의 요소를 선택하여 피벗 설정
# 피벗을 기준으로 리스트를 두의 리스트로 분ㄹ
# 1. 피벗보다 작은 요소
# 2. 피벗보다 큰 요소
# 재귀적 퀵 정렬
# 서브리스트 정렬
