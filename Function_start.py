# function =   def is a keyword of function  then we write function name(may be user defined) then pass  argument with brakets then coloum ':'

# simple function
def my_fun():
     print("gla class")

# def prime_or_not(number):
#     for i in range(2,number):
#         if number%2==0:
#             return false
#     else:
#         return true



# sum of two numbers only function body with logic
def sum(x,y):
    sum=x+y
    return sum




# addition of two number
def sum_two(num1,num2):
    sum=num1+num2
    return sum
num1=10
num2=20
res=sum_two(num1,num2)
print(res)


def type_sum(v1,v2):
    type1=[int,list,str,tuple]
    type2=[dict,set]
    if type(v1) in type1 and type(v2) in type1:
        res =v1+v2
        return f'value is ordered or integer number,sum if {res}'
    else:
        v1.update(v2)
        return f'values are unordered merge file {v1}'
value1 =eval(input('enter the first value'))
value2=eval(input('enter the second value'))
print(type_sum(value1,value2))


# Scope of variable

????



# LAMBDA  FUNCTION
# using simple function
def pow(t):
    return t**2
n=10
res=pow(n)
print(res)

# using lambda function
pow=lambda x:x**2
print(pow(10))


# convet fto c using lambda
f_to_h=lambda x: (x-32)/1.8
fah=int(input("enter the value"))
print(f_to_h(fah))



# a=[10,20,20,30,40,1,5,50,151,14]
#
# add = lambda x:x+3
# res=tuple(map(add,a))
# print(res)

out = list(map(lambda x: 'special variable' if x>50 else 'normal variable',a))
print(out)




lst=[("laxman"),('kumar'),('vashisth'),('ram'),("seeta")]
lst.sort(key=lambda x:x[1])
print(lst)



# sum using lambda funct.
sum=lambda x,y,z:x+y+z
print(sum(10,15,14))



# MAP
# FILTER
# SHORT/SHORTED()
# MIN/MAX()
# REDUCE



#1. MAP FUNCTION= ek ek quantity ko leker use change krta h or ise hm type cast kr ke dekhte h . isme do armument hote h. map(functionname,sequence data)

# example1
k=['3','42','32','44']
out=list(map(lambda y: "4"+y,k))
print(out)
# ['43', '442', '432', '444']



# exmanple 2
k=[1,22,45,5,69,55,7,4,22]
out=list(map(lambda x:x+2,k))
print(out)
# [3, 24, 47, 7, 71, 57, 9, 6, 24]




#2.FILTER = iska use hmm condition me krte h mtlb jb hamare pass true or false ki condition hongi tb hmm filter ka use krenge otherwise map ka.

# map or filter ka syntax same h or show krne ka arika bhi.
# Example 1
k=[12,25,47,96,32,55]
out=list(filter(lambda x:x>20,k))
print(out)
# [25, 47, 96, 32, 55]




# Example 2
k=[14,2,58,78,64,32,88,1,17]
print(list(filter(lambda x:x%2==0,k)))
# [14, 2, 58, 78, 64, 32, 88]



# Diffferce between filter and map = map gives true and false bt filter gives value show example bleow.
# through maps
k=[12,41,58,66,99,22,77,54,268,2348,112,257]
out=list(map(lambda x : x > 40 , k))
print(out)
# [False, True, True, True, True, False, True, True, True, True, True, True]




# through Filter
k=[12,41,58,66,99,22,77,54,268,2348,112,257]
out=list(filter(lambda x : x > 40 , k))
print(out)
# [41, 58, 66, 99, 77, 54, 268, 2348, 112, 257]


out=sorted(k,key=lambda x:x%2==0)
print(out)