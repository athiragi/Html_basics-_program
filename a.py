def rec(k):
    if(k>0):
        result=k+rec(k-1)
        print(result)
    else:
        result=0
    return result
print("the r")
rec(6)