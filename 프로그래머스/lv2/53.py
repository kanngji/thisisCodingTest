# 호텔대실

def time2val(time):
    return int(time[:2])*60+int(time[3:5])
def solution(book_time):
    dic={}
    for book in book_time:
        st= time2val(book[0])
        en= time2val(book[1])
        for t in range(st,en+10):
            if dic.get(t)==None:
                dic[t]=1
            else:
                dic[t]+=1
                
    print(dic)
    return max(dic.values())