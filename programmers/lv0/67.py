def solution(bin1, bin2):
    answer = ''
    bin1=int(bin1,2)
    bin2=int(bin2,2)
    bin3=bin(bin1+bin2)
    return bin3[2::]