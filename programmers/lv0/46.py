def solution(hp):
    answer = 0
    attack=[5,3,1]
    i=0
    while hp!=0:
        answer+=hp//attack[i]
        hp=hp%attack[i]
        
        i+=1
    return answer