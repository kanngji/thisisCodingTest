# 겹치는 선분의 길이

def solution(lines):
    sets= [set(range(min(l),max(l))) for l in lines]
    
    return  len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    print(sets)

# https://velog.io/@damin1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%B9%EC%B9%98%EB%8A%94-%EC%84%A0%EB%B6%84%EC%9D%98-%EA%B8%B8%EC%9D%B4