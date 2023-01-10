def solution(my_string):
    answer = ''
    for i in my_string:
        if i== 'a':
            
            continue
        elif i =='e':
            continue
        elif i =='o':
            continue
        elif i =='u':
            continue
        elif i =='i':
            continue
        else:
            answer+=i
    return answer


# 다른 사람 풀이
def solution(my_string):
    answer = ''

    for c in my_string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            continue
        answer += c

    return answer

# 다른 사람 풀이

def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string