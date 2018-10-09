#Strings are immutable
s='abc'
#can't delete a character in s.
s1=s.replace('b','h') #s1='ahc', s='abc'

#flatten list of strings to string
 z=['a',"One"]
 s=''.join(z)
 print(s) #prints aOne

#flatten list of integers to string
z=[1,2,3,4,5]
z_str=''.join(str(i) for i in z)
print(z_str) #prints '12345'

#flatten list of lists to list
list=[[1,2],[2,3],[3,4]]
l=sum(list,[]) #[1, 2, 2, 3, 3, 4]

#How to get value of a given key
d={1:2,2:2,4:1}
#print(d.keys()[d.values().index(1)]) #Python 2
print(list(d.keys())[list(d.values()).index(1)]) #Python 3

helloworld=['hello','world']
nums=[1,2]
d=dict(zip(helloworld,nums)) #{'hello': 1, 'world': 2}
c, v =  zip(*d) #c='hello','world' and v=1,2

 h=['hello','world',1,2]
new=dict(zip(h[0::2],h[1::2])) #{hello:world, 1:2}

# This example is applicable to lists, tuples and sets as well
x = 'computer'
print(x[-1]) #prints 'r'(last element)
print(x[-3:]) #prints 'ter'
print(x[:-2]) #prints 'comput'

x = 'horse' + 'shoe'
print(x) #prints horseshoe
x = ['pig','cow'] + ['horse']
print(x) #prints ['pig', 'cow', 'horse']

x = 'bug' * 3
print(x) #bugbugbug

x = [8,5] * 3
print(x) #[8,5,8,5,8,5]

x = 'bug'
print('u' in x) #prints True
x = ['pig','cow']
print('pig' not in x) #prints False

x = [7,8,3]
for i in x:
    print i #prints 7 8 3

for i,item in enumerate(x):
    print i,item #prints 0 7, 1 8, 2 3

#min : Can only use with same type(letters or numbers but not mixed)
#max similar to min
x = 'bug'
print(min(x)) #prints 'b'
x = ['pig','cow']
print(min(x)) #prints 'cow'

#Sum : Can only use with numbers
x = [2,5,8,12]
print(sum(x)) #prints 27
print(sum(x[2:])) #prints 20

#Sorted: returns a sorted list, does not change original list
x='bug'
print(sorted(x)) #prints 'b','g','u'
x = ['pig','cow']
print(sorted(x)) #prints 'cow','pig'

#Sort : sorts the original list in place
x=[1,2,3,4]
x.sort() #now x is [4,3,2,1]

#random
x=[1,2,3,4]
import random
from random import choice
print(choice(x))

from random import randrange
print(randrange(0,10)) #prints a random number between 0 and 9

#Count
x = 'hippo'
print(x.count('p')) #prints 2
x = ['pig','cow','cow']
print(x.count('cow')) #prints 2

#Index : Returns first index of the item in list
x = 'hippo'
print(x.index('p')) #prints 2
x = ['pig','cow','cow']
print(x.index('cow')) #prints 1

#Unpacking
x = ['pig','cow','cow']
a,b,c = x #a='pig', b and c = 'cow'

#list comprehension
x = [z**2 for z in range(10) if z>4]
print(x) #[25,36,49,64,81]

#delete
x = [2,5,8,12]
del(x[1]) #deletes 5
del(x) #deletes the entire list

#append
x = [2,5,8,12]
x.append(7) #[2,5,8,12,7]
y=[1,2]
x.extend(y) #[2,5,8,12,7,1,2] Same as + function

#insert
x = [2,5,8,12]
x.insert(1,3) #[2,3,5,8,12]
x.insert(1,['a','b']) #[2,['a','b'],3,5,8,12]

#pop
x = [2,5,8,12]
print(x.pop()) #prints 12

#remove
x = [2,5,8,12,5]
x.remove(5) #[2,8,12,5] Removes 1st 3

#reverse
x = [2,5,8,12]
print(x.reverse()) #[12,8,5,2]

#tuple
x=()
x=(1,2,3)
#can't delete an item
x=(1,[2,3],4)
del(x[1]) #error
del(x[1][1]) #works! prints (1,[2],4)

#set
x.add(item)
x.remove(item)
item in x
x.pop() #returns a random element
x.clear()
set1&set2 #intersection
set1|set2 #union
set1^set2
set1-set2
set1<=set2 #set2 contains set1
set1>=set2 #set1 contains set2

#dict
x = {'a':1, 'b':2, 'c':3}
x = dict(a=1,b=2,c=3)
x['d'] = 4 #adds 'd':4
x['b'] = 5 #updates 'b':5(from 2)
item in x
item not in x
x.clear()
del(x)

x.keys()
x.values()
x.items()
item in x.values()
for key in x:
    print key #print key
	print x[key] #print value

for k,v in x.items():
    print k,v


