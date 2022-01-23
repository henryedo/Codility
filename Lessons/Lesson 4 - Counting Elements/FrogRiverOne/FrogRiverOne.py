def solution(X, A):
    setList = set()
        
    for i in range(1, X+1):
        setList.add(i)

    for j in range(0, len(A)):
        if A[j] in setList:
            setList.remove(A[j])
                
        if len(setList) == 0:
            return j
        
    return -1
    pass
