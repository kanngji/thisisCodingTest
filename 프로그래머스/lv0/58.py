def solution(numbers, direction):
    answer = []
    empty=['']
    if direction =="right":
        numbers=empty+numbers
        numbers[0],numbers[-1]=numbers[-1],numbers[0]
        numbers.pop()
        answer=numbers
    else:
        numbers=numbers+empty
        numbers[0],numbers[-1]=numbers[-1],numbers[0]
        answer=numbers[1::]
        
    return answer