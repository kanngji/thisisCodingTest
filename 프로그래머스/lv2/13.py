# 뒤에 있는 큰 수 찾기

def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]<numbers[j]:
                answer.append(numbers[j])
                break
        else:
            answer.append(-1)
    answer.append(-1)
    return answer

# 시간 초과
