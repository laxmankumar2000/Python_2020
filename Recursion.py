# countdown  using recursion

import time

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
countdown(5)
print("happy recursion day")



# factorial

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*fact(n-1))

print(fact(5))



# gcd

def gcd(a,b):
    if a>b:
        print(a-b,b)
        return gcd(a-b,b)
    elif b>a:
        print(a,b-a)
        return gcd(a,b-a)
    else:
        print(b)
        return b
num1=eval(input("enter the 1st value"))
num2=eval(input("enter the 2nd value"))
res=gcd(num1,num2)
print(res)


# min swure in rectangle

def min_sqr(a,b,c=0):
    if a>b:
        c+=1
        print(a,b,c)
        return min_sqr(a-b,b,c)
    elif b>a:
        c+=1
        print(a, b, c)
        return min_sqr(a,b-a,c)
    else:
        print(a, b, c)
        return c+1

print(min_sqr(5,2))


# revers string

def rvs_str(s):
    if s=="":
        print(s)
        return ""
    else:
        print(s)
        return rvs_str(s[1:]) + s[0]
str=eval(input("enteer the string"))
res=rvs_str(str)
print(res)




def sum(num1):
    if num1==1:
        return 1
    else:
        return num1 + sum(num1-1)
print(sum(int(input("pls enter th enum"))))


