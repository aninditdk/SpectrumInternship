n=int(input())
lst=[]
def prime(m):
    k=0
    for i in range(1,m):
        if m%i==0:
            k+=1
    if k==1:
        return True
    else:
        return False
for i in range(n):
    if prime(i):
        print(i)
if prime(n):
    print("the given input number {} is a prime number".format(n))
else:
    print("the given string is not a prime number")
