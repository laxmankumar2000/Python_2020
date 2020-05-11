''''
 QUE.1..   what is set ??
 $$ set is a unordered collection of item. Every element is unique and must be immutable(not changeable), however sets are mutable.
 $$ sets can used to perform mathmatical opertaion like Union,Intersection etc...

 QUS.2..   How to create set??
 $$ A set can be creted by placing all items inside curly bracess {}, sepraetes by comma, or by using built in function set().
 my_set={1,2,3}
prnt(my_set)




'''



# initilization of sets
# 1.empty set
s=set()                       #using constructor
print(s,type(s))              # set() <class 'set'>


# 2.with single item
s={7}
print(s,type(s))              # {7} <class 'set'>


# 3. By eval()
s=eval(input("pls enter your set"))
print(s,type(s))              # {'hii'} <class 'set'>


# 4.by type casting
s=set('hello')
print(s)                       # {'l', 'o', 'h', 'e'}



# 5.by using loop
s=set(range(1,20))
print(s)                       # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}





# sets properties
# 1.sets are mixes data type
s={1,2,3,'hii',(14,12) }
print(s)                        # {1,2,3,'hii',(14,12),1}


# 2.sets have not duplicate items
s={1,2,3,'hii',(14,12),1,2,3}
print(s)                        # {1,2,3,'hii',(14,12),1}


# 3.you cannot have mutable items in sets
s={1,2,3,'hii',(14,12),['hello',2,5]}
print(s)                          # TypeError: unhashable type: 'list'


# 4.in set mutabkle item not support bt we can type cast a setfrom list
s= {'laxman'}
print(s,type(s))                   # {'laxman'} <class 'set'>




# methods of sets === there are 17ethods in python set .


# 1. add() = Add elememt in set file. if element allready presnet in set then it notgive any error.
# $$ syntax= set_name.add(elemet)
s={1,2,3,4,5}
 s.add(6)
 print(s)                                 # {1, 2, 3, 4, 5, 6}
 print(s.add(7))                            # None
s.add(2)
print(s)                                    # {1, 2, 3, 4, 5,6}

s={2,5}
s.add(2.0)
s.add(5.01)
s.add('hello')
print(s)                                    # {2, 'hello', 5, 5.01}

'''
s=set()
for i in range(5):
    s.add(int(input('s')))
print(s)

'''



# 2.clear() = Remove All element from the set
s={1,2,4,'hii'}
s.clear()
print(s)                                             # set()




# 3. copy() = Return copy of set.
# %% Syntax =  set_name.copy()
s={'hii',58,647}
l=s.copy()
print(s,id(s))                                       #{58, 'hii', 647} 2853396740576
print(l, id(l))                                       #{58, 'hi', 647} 2853396559904



# 4.Differnce() = Return the dffernce pf two or more sets asa a new set
s1={1,2,3,4,5,6,7,8,9}
s2={3,5,7,9}
s3=s1.difference(s2)
print(s3)                                               # {1, 2, 4, 6, 8}



# 5.Difernce_Update() = remove all element another set from this set
# $$  Syntax = set_name.differnce_update(set name)
s1={5,6,7,8,9}
s2={3,10,7,9}
# s1.difference_update(s2)
s1.difference(s2)
print(s1)



# 6.Discard() =remove element from set if it is memeber(if element is not present then do nothing)
# $$ syntax. = set_name.deicard(element)
s={1,2,5,8,'hallo'}
s.discard(2)
print(s)                                           # {1, 5, 8, 'hallo'}
s.discard(7)
print(s)                                           # {1, 5, 8, 'hallo'}



# 7.Intersection() = Return intersection of two set in a new set
# $$ syntax =
s1={1,2,3,4,5,"hii",7,8}
s2={5,'hii',59,33,475}
s3=s1.intersection(s2)         #Method
# s3=s1 & s2                    Expression
print(s3)                                           # {'hii', 5}



# 8.Intersection_update() = update set with intersection of itself and another
s1={1,2,3,4,5,'hii',7,8}
s2={5,'hii',59,33,475}
s1.intersection_update(s2)
print(s1)                                           # {'hii', 5}



# # 9.Isdisjoint() = Return True if in two set have null intersction.
# # $$ Syntax = set_name.isdisjoict(set_name)
# s1={3,5,7,9}
# s2={2,4,6,8}
# s1.isdisjoint(s2)
# print(s1)



# 10.issubset() = Return 'TRUE' if all element of set are present in another set , otherwise 'FALSE'
# $$ Syntax = set_name(check).issubset(set_name(universal))
s1={1,2,3,5,9,8,7,4,6,"hiii"}
s2={3,5,7,9,'hiii'}
s3=s2.issubset(s1)
print(s3)



# 11.?????????/



# 12.Pop() =removees anda return an arbitary set element and remove random. it genrate key error if set is empty
# $$ syntax = set_name.pop()
s={'a','b',1,5,9}
s.pop()
print(s)                                # {5, 9, 'b', 'a'}



# 13.Remove ) = Search forr given element and remove it. if eleemt is not thier it gives keyerror
# $$ syntax = set name.remove(element that remove)
s={1,2,3,5,'hiii'}
s.remove("hiii")
print(s)                               # {1, 2, 3, 5}



# 14.union() = return union of two set in  a new set..
s={1,2,5,8,'hii'}
s2={9,7,3,4,'laxman'}
s3=s.union(s2)
s.union(s2)                             # it gives s1????????////
print(s3)                             # {1, 2, 3, 4, 5, 7, 8, 9, 'hii', 'laxman'}



# 15.Update() =








