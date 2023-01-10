def solution(a, b):
    answer = 0
    # zip() 기본 문법
    # numbers=[1,2,3]
    # letters=["A","B","C"]
    # for pair in zip(numbers,letters):
        # print(pair)
    for pair in zip(a,b):
        answer+=pair[0]*pair[1]
        
    return answer