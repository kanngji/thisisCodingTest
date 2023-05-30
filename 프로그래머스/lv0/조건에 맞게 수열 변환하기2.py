def solution(arr):
    answer = -1
    copy_arr=[0]*len(arr)
    
    while copy_arr!=arr:
        answer+=1
        
        # 그냥 copy_arr=arr 하면 얉은 복사 되서 안된다
        for i in range(len(arr)):
            copy_arr[i]=arr[i]
        for i in range(len(arr)):
            if arr[i] >=50 and arr[i]%2==0:
                arr[i]=arr[i]//2
            elif arr[i]<50 and arr[i]%2==1:
                arr[i]=arr[i]*2+1
        
        
        
    
    return answer