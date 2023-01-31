# 기사단원의 무기

def solution(number, limit, power):
    answer = 0
    arr=[]
    # 일단 약수의 개수 구하기
    for i in range(1,number+1):
        cnt=0
        for j in range(1,number+1):
            if i%j==0:
                cnt+=1
        arr.append(cnt)
    for i in range(len(arr)):
        if arr[i]>limit:
            arr[i]=power
    return sum(arr)

# 시간초과 나서 다른사람 풀이 봄
def get_cds(n, limit , power):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): # ★포인트1. 제곱근만큼만 반복
        if n%i == 0:
            if i == n//i: # 제곱근일 경우 -> 1개만 카운트하기
                cnt += 1
            else:
                cnt += 2 # 제곱근이 아닐 경우, 2개 카운트 (i, n//i)
        if cnt > limit:  # ★포인트2. 소수의 개수가 limit를 넘어가면
            return power #            강제로 power만큼을 return 
    return cnt

    
def solution(number, limit, power):
    total = 1
    for i in range(2, number+1):
        len_cds = get_cds(i, limit, power)
        total += len_cds

    return total