#sorted 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

# sort 소스코드

array1 = [7,5,9,9,3,1,6,2,4,8]

array1.sort()
print(array1)


# 정렬 라이브러리에서 key를 활용한 소스코드
array3 = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[0] # data[0] 으로 하면 첫번째 원소 ㄱ ㄴ ㄷ #data[1] 로 하면 두번째 원소 1 2 3

result = sorted(array3, key=setting)
print(result)


