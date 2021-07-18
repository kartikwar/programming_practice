"""
Implementation of heap sort (ascending) in python
sort an array (ascending order) using the heap data structure
in a heap data structure the parent node is always greater 
than or equal to the child node  
"""

def heapsort(A):
   #start heapifying from bottom to top
   build_max_heap(A)
   #once its heapified properly, start heapyfying from top to bottom 
   # since swap happens b/w top and bottom only
   for i in range(len(A) - 1, 0, -1):
       A[0], A[i] = A[i], A[0]
       max_heapify(A, index=0, size=i)

def parent(i):
   return (i - 1)//2

def left(i):
   return 2*i + 1

def right(i):
   return 2*i + 2

def build_max_heap(A):
   length = len(A)

   start = parent(length - 1)
   while start >= 0:
       max_heapify(A, index=start, size=length)
       start = start - 1

def max_heapify(A, index, size):
   left_child = left(index)
   right_child = right(index)
   if (left_child < size and A[left_child] > A[index]):
       largest = left_child
   else:
       largest = index
   if (right_child < size and A[right_child] > A[largest]):
       largest = right_child
   if (largest != index):
       A[largest], A[index] = A[index], A[largest]
       max_heapify(A, largest, size)


A= [4,10,3,5,1,6,7]

A = [int(x) for x in A]
heapsort(A)
print('Sorted list: ', end='')
print(A)