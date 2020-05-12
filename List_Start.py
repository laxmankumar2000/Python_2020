'''                                                     list

Qus.1..Explain  list??
$$ List is a data structure in PYTHON that is mutuable and changeable,orderd sequence of element. Each element or value that is inside
    of a list is called 'AN ITEM'.List are defined by having values between 'SQUARE BRACKET' '[]'.
        EX- lst=['laxman',254,'corgi']

Properties of LIST
$ ordered -- each element have fixed postion in alist.
$ iterable -- yor can get their elemnt on eby one.
$ able to store duplicates values.
$ able to store differnt types of elements.

Qus.2.. Why list is mutable??
$$  k=[2,43,1,78]
    % item assignment is allowed
        k[-1]=100
        print(k)                [2,43,1,78,100]
    % add or append items at run time.
        k.append(29)
        print(k)                 [2,43,1,78,100,29]
    % delete at run time.
        del k[0]
        print(k)                 [43,1,78,100]
    % remove item from starting.
        k.remove(1)
        print(k)                [43,78,100]

 Qus.3.. How to accessing the element on ist??
 $$  By Using Indexing -- Get the single element
        st=[1,3,43,4]
        d=st[0]
        print(s)                     1

     By usinh Slicinh 00k gest the sublist ..
         st =[1,4,5,32,5]
         d=st[0:3]
         print(d)                    [1,4,5]



'''

# Initialize the list (empty list)
ls = []
ls = list()
print(type(ls),type(lst))                                       #<class 'list'> <class 'list'>


st = range(10)
ls = list(st)
print(st)                                             #range(0, 10)
print(ls)                                            #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Indexing -- get the element at given position.

ls = [1,3,65,['hello',59],60]
out1 = ls[2]
out2 = ls[3][0]
print(out1)                                           # 65
print(out2)                                           # hello




# Slicing -- Get the subsequnce (sub list) at given range.

ls = [1,3,65,['hello',59],60]
out = ls[1:4]
print(out)                                              # [3, 65, ['hello', 59]]



# changeable item update.

lst = [3, 65, ['hello', 59]]
lst[0] = 'laxman'
print(lst)                                               # ['laxman', 65, ['hello', 59]]


# Methods of list..

# Adding element methods.

    # 1. Append() -- Add in a element in a list.

        ls = [2,4,6,8,10]
        ls.append(13)
        print(ls)                                         #[2, 4, 6, 8, 10, 13]
            # if element allready is present
            ls.append(8)
            print(ls)                                     # [2, 4, 6, 8, 10, 8]



    # 2.Extend() -- Append iterable values in a list individual.

        lst = [2,4,5,8]
        lst.append(10)
        lst.extend("hello")
        print(lst,len(lst))                                           # [2, 4, 5, 8, 10, 'h', 'e', 'l', 'l', 'o'] 10


    # 3. insert() - - Adds the element in a specified position. it have only 2 Argument.

        ls = [2,4,6,8,"python"]
        ls.insert(4,'laxman')
        print(ls)                                           # [2, 4, 6, 8, 'laxman', 'python']



# Remove methods
    # 4. clear() - Remove all the element in list. it takes no argumnet.
        ls = [1,3,4,6,8,7,]
        ls.clear()
        print(ls)                                           #[]   emepty ist


    # 5. remove() -- Remove the item from speified value. takes one argument.

        ls = ["laxman",45,'kumar']
        ls.remove(45)
        print(ls)                                            #['laxman', 'kumar']


    # 6.POP() - - Remove he item from specified postion . takes one argument.

        ls = [2,4,8,6,78,'python']
        ls.pop(2)
        print(ls)                                             # [2, 4, 6, 78, 'python']



# 7.copy() -- Return a copy item in new list. the id of both list is diffrenet.

        ls = [1,2,5,8,59]
        ls1=ls.copy()
        print(ls,id(ls))                                      # [1, 2, 5, 8, 59] 2259017946432
        print(ls1,id(ls1))                                    # [1, 2, 5, 8, 59] 2259028609728


# 8.Reverse() --  Reverse the order of list.

        ls = [1,2,5,8,59]
        ls.reverse()
        print(ls)                                             # [59, 8, 5, 2, 1]


# 9.Count() -- Return the number of element with specified value.take 2 argument.

        ls = [1,2,5,7,9,2,5,1,7,9,1]
        out = ls.count(1)
        print(out)                                            # 3



# 10.index -- Return the index of first element with specified value.

        ls = [2,5,6,3,5,1,2,7,4,8,9,1,2]
        out1 = ls.index(1)
        out2 = ls.count(1)
        print(out1)                                            # 5
        print(out2)                                            # 2

# 11.Sort() -- Sort the list. take 3 agrument  self,key reverse
#         1. Sort with number.
                ls = [2,4,6,8,49,0]
                out1 = ls.sort()
                out2 = ls.sort(reverse = True)
                print(out1)
                print(out2)                                     # [49, 8, 6, 4, 2, 0]

        # 2.Sort with string ascii.
                ls = ['rAvi','akash','aNjali','Zebra','tarun']
                ls.sort()
                print(ls)

        # 3.Sort with function.
                ls = ['ravi',['akash','aNjali'],'Zebra','Tarun']
                ls.sort(key=len)
                print(ls)                                       # [['akash', 'aNjali'], 'ravi', 'Zebra', 'Tarun']

        # 4.Sort with string max char in length.
                ls = ['ravi','akash','aNjali','Zebra','Tarun','aa','AA']
                ls.sort(key=max)
                print(ls)                                       # ['AA', 'aa', 'aNjali', 'Zebra', 'akash', 'Tarun', 'ravi']



