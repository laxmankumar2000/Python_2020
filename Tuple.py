'''
                                                        TUPLE
QUS.1.. Explain Tuple?
$$ Tuple is an ordered cpllection of objects and defined by encosing the element in parenthesis() instead
of squre brackets([]), and it is also immutable(not changavle)

    The differnce between list oand tuple are, the tuple can not be changed unlike list. Tuple use parenthesis but
    list are squre bracket[].



'''

# Initialization the tuple.
t=()
print(type(t))                              # <class 'tuple'>

# t=tuple()  #constructor



# Initizlize the tuple with single element.
b=(20,)
a=20,
print(a,type(a))                           # (20,) <class 'tuple'>



# Tuple Operation.
    # 1. Indexing: Element a position.
    t=(2,43,'hello',[2,43])
    d=t[2]
    print(d,type(d))                           # hello <class 'str'>


    # 2.Slicing: Element at given range.
    t=(2,43,'hello',[2,43])
    d=t[1:4]
    print(d,type(d))                            #(43, 'hello', [2, 43]) <class 'tuple'>




# Item assignment: it gives error because it is immutable.
    t=(2,43, 'hello', [2, 43])
    t[0]=5
    print(t)                        # ypeError: 'tuple' object does not support item assignment


    # Item deletion
    t=(2,43, 'hello', [2, 43])
    del t[2]
    print(t)                         # TypeError: 'tuple' object doesn't support item deletion


    # List in tuple
    t=(2,43, 'hello', [2, 43])
    t[2].append('hi')
    print(t)                           # AttributeError: 'str' object has no attribute 'append'
    t[1].clear
    print(t)                            # AttributeError: 'int' object has no attribute 'clear'




# Tuple creation with multiple element number.
    # using Tuple construtor or type cast.
        t=tuple(range(1,20))
        print(t)                             # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)


    # Using concat
        t=()
        for i in range(1,20):
        t+=i
        print(t)                                # TypeError: can only concatenate tuple (not "int") to tuple


        t=()
        for i in range (1,21):
        t += (i,)                       # two tuple are concat. tuple not concat with any other(list string )
        print(t)                                    # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)




# Tuple genrator.
l=(i for i in range(1,10))
print(l,type(l))                    # <generator object <genexpr> at 0x000001A602B33580> <class 'generat

tp=tuple(l)
print(tp,type(tp))                  # 1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>



# Tuple with  other operations.
    # 1.Membership.
        t=(1,2,3,4,5,6,7,8,9,10)
        item=1
        out=item in t
        print(out)                                # True
        item=50
        out2=item in t
        print(out2)                                             # False


    # 2.Multipication with number =
        t=(1,2,3)
        out=t*3
        print(out)                                      # (1, 2, 3, 1, 2, 3, 1, 2, 3)


    # 3.Addition (concat)
        t1=(2,4)
        t2=(4,6)
        out=t1+t2
        print(out)                                      # (2, 4, 4, 6)


    # 4.Iteration with tuple(tenaverse)
        t=(2,59,'hii')
        for i in t:
        print(i)
        # 2
        # 59
        # hii




# Methods in Tuple.
    # 1.index.Return match index of each eleemtn.
        t=('a','b',2,5)
        out=t.index('b')
        print(out)                                      # 1

        out=t.index('hello')
        print(out)                                      # ValueError: tuple.index(x): x not in tuple



    # 2.countcountthe frequrncy of elelemtn in tuple.
        t=(1,2,5,7,6,3,1,5,4,8,9,3,6,78,5)
        out=t.count(5)
        print(out)                                      # 3



