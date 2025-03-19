
def cube(n) :
    print(n*n*n)

def by_3(n) :
    if (n%3==0) :
        return cube(n)
    
    else :
        print("input not valid")

n = int(input("enter a number"))

by_3(n)