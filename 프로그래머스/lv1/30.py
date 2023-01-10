# 최소 직사각형

# 각 w,h를 비교해서 둘 중 큰 값을 한 리스트에 넣고 나머지를 리스트에 넣는다
# 두 개의 리스트 중 가장 큰 값을 뽑아서 곱하면된다.


def solution(sizes):
    answer = 0
    w=[]
    h=[]
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])
    return max(w)*max(h)

# 다른 사람 풀이

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
