# k번째 수
def solution(array, commands):
    answer = []
 
    for x in range(len(commands)):
        i=commands[x][0]
        j=commands[x][1]
        k=commands[x][2]
        arr=array[i-1:j:]
        arr.sort()
        answer.append(arr[k-1])
    return answer