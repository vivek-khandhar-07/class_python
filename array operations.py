#1 len() - number of elements

from array import array
arr = array('i',[10,20,30,40,50])
print(len(arr))

#2 append(x) - add element at end 

from array import array
arr = array('i',[10,20,30])
arr.append(40)
print(arr)

#3 insert(pos,x) - insert at postion

from array import array
arr = array('i',[10,20,30,40])
arr.insert(2,30)
print(arr)

#4remove(x) - remove first occurence

from array import array
arr = array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)

#5 pop() - remove and return last element

from array import array
arr = array('i',[10,20,30,40])
x = arr.pop()
print("removed :",x)
print(arr)

#6 index(x) - find index of element

from array import array
arr = array('i',[10,20,30,40])
print(arr.index(30))

#7 count(x) - count occurrences

from array import array
arr = array('i',[10,20,30,20,40])
print(arr.count(20))

#8 reverse() - reverse array

from array import array
arr = array('i',[10,20,30,40])
arr.reverse()
print(arr)