def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 중간 지점을 기준으로 리스트를 두 부분으로 나눕니다.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 각 부분 리스트를 재귀적으로 병합 정렬합니다.
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 두 정렬된 리스트를 병합합니다.
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # 두 리스트의 요소를 하나씩 비교하여 작은 것을 결과 리스트에 추가합니다.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 남아 있는 요소들을 결과 리스트에 추가합니다.
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 예제 리스트
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = merge_sort(arr)
print(sorted_arr)