def oddNumber(n):
    print(n)
    if n>0:
        oddNumber(n-1)
        print(n)
        # print(2*n-1)
print(oddNumber(9))