# 체스판 다시 칠하기

n,m = map(int,input().split())

mtr = []
cnt = []

for i in range(n):
    mtr.append(input())

for a in range(n-7):
    for b in range(m-7): # 8*8로 자르기 위해, -7 해준다
        w_index=0 # 흰색으로 시작
        b_index=0 # 검은색으로 시작
        for i in range(a,a+8): #시작 지점
            for j in range(b,b+8): #시작 지점
                if (i+j)%2==0: # 짝수 인경우
                    if mtr[i][j]!='W': # W가 아니면, 즉 B이면 
                        w_index+=1 
                    else:
                        b_index+=1
                else: #홀수 인 경우
                    if mtr[i][j]!='W':
                        b_index+=1
                    else:
                        w_index+=1
        cnt.append(w_index)
        cnt.append(b_index)
print(min(cnt))