def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')

print(printN(10))