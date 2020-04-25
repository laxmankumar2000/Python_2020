# empty dictionary
d={}
print(type(d))                 # <class 'dict'>



d=dict()
print(d,type(d))                # {} <class 'dict'>



# how to make dictionry:  sct_name={keys:valeus,keys:value................}
# ex.     dct={'name':'kumar','sec.':'a'....}
l=["laxman",59,"sec.A","GLA UNIVERSITY"]
print(l[0])                    # laxman


d={'name':['laxman','sanskar'],'roll no.':59,'section':'A','institute':"gla"}
print(d['name'])                  # ['laxman', 'sanskar']



# Dictionary operations
dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59}
print(dct,type(dct))                 # {'name': 'laxman', 'cpi': 81.6, 'sec': 'A', 'roll': 59} <class 'dict'>

d=dct['roll']
print(d,type(d))  # Accinssing the element                    # 59 <class 'int'>
d1=dct['address']
print(d1,type(d1))                                    # Key error bcus name does not exits



# imp thing= keys are unique othrwise it upgrade second one bt values are not unique
# ex1 for keys
dct={'name':'laxman',"add":'doon','name':'kumar'}
print(dct)                              # {'name': 'kuamr', 'add': 'doon'}
# ex2
dct={'name': 'kuamr', 'add': 'doon' , 'sirname':'kumar'}
print(dct)                              # {'name': 'kuamr', 'add': 'doon', 'sirname': 'kumar')




# update
dct["name"]='kumar'
dct["address"]="dehradoon"
print('after update',dct)                   # after update {'name': 'kumar', 'cpi': 81.6, 'sec': 'A', 'roll': 59, 'address': 'dehradoon'}




# keys(): get all keys of dictionary
dct={'name':'chanchal','age':19.7,'roll':32,'cpi':86}
out1=dct.keys()
print(out1,type(out1))                         # dict_keys(['name', 'age', 'roll', 'cpi'])   <class 'dict_keys'>
print(list(out1),type(out1))                    # ['name', 'age', 'roll', 'cpi'] <class 'dict_keys'>




# values(): to get all values of dictonary

out2=dct.values()
print(out2,type(out2))                               # dict_values(['chanchal', 19.7, 32, 86]) <class 'dict_values'>



# delete element
dct={'name':'chanchal','age':19.7,'roll':32,'cpi':86}
del dct['name']

print(dct)                     #{'age': 19.7, 'roll': 32, 'cpi': 86}
dct['name']='laxman'
print(dct)                     # {'age': 19.7, 'roll': 32, 'cpi': 86, 'name': 'laxman'




# dictionary methods

# 1.python dictionay clear() = remove all items

dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
# print(dct,id(dct))                        # 492234329664
dct.clear()
print(dct,id(dct))                                 # {} 492234329664




# 2. python copy () = return shalloe copy of dictionary

dct = {'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
dct2=dct.copy()
print(dct2)

dct2.clear()
print(dct2)                           # {}
print(dct)                            # {'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}







# 3.python dictionary get() = retrun value of the key                    if keys not present it gives

dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
out1=dct.get("address",'na')
print(out1)                      # doon
out2=dct.get("ddress")
print(out2)                      # none
out3=dct.get("address1",'na')
print(out3)                      # na





# 4. python dictonary fromkey = create dictionay from given sequence

dct= {'name','cpi','sec','roll','address','institute'}
out1 = dict.fromkeys(dct,0)
print(out1)                      # {'name': 0, 'address': 0, 'sec': 0, 'roll': 0, 'cpi': 0, 'institute': 0}






# 5. python dictionary items() = return view of dictionary(keys , value) in pair

dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
out1=dct.items()
print(out1)  # dict_items([('name', 'laxman'), ('cpi', 81.6), ('sec', 'A'), ('roll', 59), ('address', 'doon'), ('institute', 'GLA UNIVERSITY')])





# 6. python dictionay  keys() = return all keys in a dictionary

dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
out1=dct.keys()
print(out1,type(out1))                        # dict_keys(['name', 'cpi', 'sec', 'roll', 'address', 'institute']) <class 'dict_keys'>
print(list(out1), type(out1))                 # ['name', 'cpi', 'sec', 'roll', 'address', 'institute'] <class 'dict_keys'>





#7. python dictioary values(): to get all values of dictonary

out2=dct.values()
print(out2,type(out2))                          # ict_values(['laxman', 81.6, 'A', 59, 'doon', 'GLA UNIVERSITY']) <class 'dict_values'>




# 8. python dictionary pop() = revome and return element having key mean it remove the element and then return those
#                               element which was delete/remove

dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
out1=dct.pop('name')
print(out1)                          # laxman
print(dct)                           # {'cpi': 81.6, 'sec': 'A', 'roll': 59, 'address': 'doon', 'institute': 'GLA UNIVERSITY'}





# 9. python dictioanry popitems() =  remove and retuen item from end in dictionary

dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
out=dct.popitem()
print(out)                                  # ('institute', 'GLA UNIVERSITY')
print(dct)                                   # {'name': 'laxman', 'cpi': 81.6, 'sec': 'A', 'roll': 59, 'address': 'doon'}




# 10. python dictionary setdefault() = insert a key with value if key is not present

dct={'name':'laxman','cpi':81.6,'sec':'A','roll':59,'address':'doon','institute':'GLA UNIVERSITY'}
out1=dct.setdefault("semester",1)
print(dct)    # {'name': 'laxman', 'cpi': 81.6, 'sec': 'A', 'roll': 59, 'address': 'doon', 'institute': 'GLA UNIVERSITY', 'semester': 1}





11.python dictionary update() =







d={'a':1,'b':2,'c':3}
h=d['a']
k=d.get('a')
print(h,k)



a={'z':1,'b':2}
e={'c':3,'d':4}
a.update(e)
print(a)
