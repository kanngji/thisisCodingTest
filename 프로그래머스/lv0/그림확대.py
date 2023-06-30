def solution(picture, k):
    
    
    answer=[]
    for i in picture:
        new_arr = ""
        
        for j in i:
            for _ in range(k):
                new_arr+= j
        
        for _ in range(k):
            answer.append(new_arr)
        
    return answer