from functools import*
m=int(input())
n=int(input())
def sum_product(m,n):
    a=reduce(lambda x,y:x*y if x*y<=1000 else x+y,[m,n])
    return a
print(sum_product(m,n))
