'''
                                            LIST COMPREHENSIONS.
Ques.1.. What is List comprehensions??
$$ List comprehensions provide a concise way to create a list. List comprehensions is a compelete subtitutes for the lambda function as well as the
function map(),filter(),reduce().

Syntax --
    The list comprehension starts with a '[' and ']', to help you remember that the
    result is going to be a list.

    The basic syntax is
        [ expression for item in list if conditional ]
       This is equivalent to:
        for item in list:
            if conditional:
                expression


'''

def add(a):
    if a%2 == 0:
        return a-2
    else:
        return a-1

lst = [1,2,4,8]
out = [add(i) for i in lst]
# out=map(add,lst)
print(out)     # [0, 0, 2, 6]

lst = [1,2,3,4,5,65,56]
out = [i**2 for i in lst if i%2==0 ]
print(out)                                              # [4, 16, 3136]

# celcius into fahrenheit
lst = [0,10,20,30,40]
tf = [1.8*tc+32 for tc in lst]
print(tf)

ls = ['34','21','4','76']
out = [int(i) for i in ls]              # by list comprehension
bn = list(map(int,ls))             # by map function
print(out)                         # [34, 21, 4, 76]
print(bn)                           # [34, 21, 4, 76]

'''
k=next(bn)
for i in bn:
    u=list(bn)
    print(i)




k = ['33.0', '34', '12']
gen = map(eval, k)

first = list(gen)

for i in gen:
    print(i)
second = next(gen)


k = ['33.0', '34', '12']
gen = map(eval, k)

y = a, b, c = gen
print(y)

def apnafun(k):
    return k+2

l = [2, 45, 6]
k = list(map(apnafun, l))

'''


ls = ['ravi kumer','ahandan kumar','mohan rajput','abhay kumar']
out = [i.upper() for i in ls if i.split()[-1] == 'kumar' ]
print(out)                                                                   # ['AHANDAN KUMAR', 'ABHAY KUMAR']
print(ls)                                                                    # ['ravi kumer', 'ahandan kumar', 'mohan rajput', 'abhay kumar']














