# 가장 큰수

def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    

    return str(int(''.join(numbers)))

# numbers=list(map(str,numbers)) 까지는 생각했는데..
# lambda 이것도 생각했는데
# 람다 인수를 x[0] 넣어서 str 값으로 정렬해보았느넫 ("12345" 면 x[0] 넣으면 1로 정렬해주는줄) 안되서 다른 사람 풀이봄