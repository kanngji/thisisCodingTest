def solution(my_string, num1, num2):
    answer = ''
    my_string=list(my_string)
    my_string[num1],my_string[num2]=my_string[num2],my_string[num1]
    
    answer=''.join(map(str,my_string))
    
    
    return answer