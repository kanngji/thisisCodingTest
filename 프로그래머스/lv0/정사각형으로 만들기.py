def solution(arr):
    answer = [[]]
    rows = len(arr)
    columns = len(arr[0])
    print(rows,columns)
    if rows < columns:
        for _ in range(columns-rows):
            arr.append([0]*columns)
    if rows > columns:
        for i in range(rows):
            for _ in range(rows-columns):
                arr[i].append(0)
            
    return arr