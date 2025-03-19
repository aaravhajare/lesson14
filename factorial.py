
def factorial(n) :
    '''this ia a recursive function'''

    if (n==0) or (n==1) :
        return 1
    
    else:
        return n*factorial(n-1)


n = int(input("enter a number"))
print(factorial(n))