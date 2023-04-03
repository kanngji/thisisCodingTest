# 옹알이(1)

from itertools import permutations
def solution(babbling):
    answer = 0
    speak = ["aya","ye","woo","ma"]
    word = []
    for i in range(1,len(speak)+1):
        for j in permutations(speak,i): # i는 0이 아니여야 함 1개는 무조건 들어가야함
            word.append(''.join(j))
    
    for i in babbling:
        if i in word:
            answer+=1
    return answer