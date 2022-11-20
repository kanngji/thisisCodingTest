def solution(money):
    answer = []
    total=money//5500
    answer.append(total)
    answer.append(money-(total*5500))
    return answer