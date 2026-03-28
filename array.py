# arry example

from array import array

arr = array('i',[10,20,30,40])
print(arr)
print(type(arr))

# indexing arrays

#1 positive indexing

from array import array
arr = array('i',[10,20,30,40,50])
 
print(arr[0])
print(arr[2])
print(arr[4])

#2 negative indexing

from array import array

arr = array('i',[10,20,30,40,50])

print(arr[-1])
print(arr[-2])
print(arr[-5])

#3 modify element using index

from array import array

arr = array('i',[10,20,30,40,50])

arr[2] = 35
print(arr)


#4 index error

from array import array

arr = array('i', [10,20,30])
print(arr[5])