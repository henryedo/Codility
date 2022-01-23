def solution(A):
    A.sort()

    num = 1

    for i in A:
        if(i == num):
            num += 1
        else:
            return 0
        
    return 1

    pass