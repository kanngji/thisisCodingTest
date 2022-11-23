def solution(numbers):
    
    numbers=numbers.replace("zero",'0')
    numbers=numbers.replace("one",'1')
    numbers=numbers.replace("two",'2')
    numbers=numbers.replace("three",'3')
    numbers=numbers.replace("four",'4')
    numbers=numbers.replace("five",'5')
    numbers=numbers.replace("six",'6')
    numbers=numbers.replace("seven",'7')
    numbers=numbers.replace("eight",'8')
    numbers=numbers.replace("nine",'9')
    
    numbers=int(numbers)
    
    return numbers

    # 다른 사람 풀이
    def solution(numbers):
        num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, word in enumerate(num_words):
        numbers = numbers.replace(word, str(num))
    return int(numbers)