# 타겟 넘버
def solution(numbers, target):
    answer=0
    def DFS(L,hap):
        if L==len(numbers):
            if hap==target:
                nonlocal answer
                answer+=1
            return 
        else:
            DFS(L+1,hap+numbers[L])
            DFS(L+1,hap-numbers[L])
    DFS(0,0)
    return answer

# nonlocal 알아두기
# https://juhi.tistory.com/6