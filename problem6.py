from math import*
n=int(input("how many terms do you want?"))
a,b=0,1
k=0
if n==1:
    print(a)
else:
    while k<n:
        print(a)
        n1=a+b
        a,b=b,n1
        k+=1
m=int(input("inputto check if the  number is fibonacci or not"))
def check(p):
    if int(sqrt(p))**2==p:
        return True
    else:
        return False
a=5*(m**2)
if check(a+4) or check(a-4):
    print("{} is a fibonacci no".format(m) )
else:
    print("{} is not a fibonacci no".format(m))

