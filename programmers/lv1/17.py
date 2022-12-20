# 같은 숫자는 싫어
def solution(arr):
    # list 니까 stack으로
    # 제일위 [-1]랑 arr이랑 같으면 안넣고 다르면 넣는다
    answer = []
    answer.append(arr[0])
    i=1
    while (i<len(arr)):
        if answer[-1]!=arr[i]:
            answer.append(arr[i])
            i+=1
        else:
            i+=1

    return answer