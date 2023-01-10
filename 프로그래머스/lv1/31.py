# 윤년

def solution(a, b):
    days = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE','WED']
    months = [31,29,31,30,31,30, 31, 31, 30, 31, 30, 31]
    
    return days[(sum(months[:a-1])+b)%7]

# 예제 5월 24일 구하기
# sum(months[:a-1]) 로 4월까지의 모든 날짜를 더해준다.
# sum(months[:a-1])+b 그리고 b(일에 해당) 을 더해준다.
# sum(month[:a-1]+b)%7 그렇게 다 더해준 날들을 7로 나눈 나머지를 구해준다
# days[(sum(months[:a-1])+b) %] 알고 싶은건 요일임으로 그렇게 다 더해준 날들을 
# 7로 나눈 나머지에 해당하는 요일을 찾아준다.  