# Program to sort a list using merge sort
#Reference: https://www.youtube.com/watch?v=3aTfQvs-_hA&index=8&list=PLEJyjB1oGzx2h88Tj90B5_HadLq339Cso

#Create a random array
def create_array(size = 10, max_size = 100):
    from random import randint
    array = [randint(0,max_size) for _ in range(size)]
    return array

# Merge function that merges two array after sorting them.
# This takes up and extra auxilary array.
def merge(a,b):
    index_a = 0
    index_b = 0
    aux_array = []
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            aux_array.append(a[index_a])
            index_a += 1
        else:
            aux_array.append(b[index_b])
            index_b += 1
    if index_a == len(a):
        aux_array.extend(b[index_b:])
    else:
        aux_array.extend(a[index_a:])
    return aux_array

#Merge_sort function divides the array and then passes it to the merge function.
def merge_sort(array):
    if len(array) <= 1:
        return array
    left, right = merge_sort(array[:len(array)//2]), merge_sort(array[len(array)//2:])
    return merge(left,right)
    
array = create_array()
print("Unsorted array:\t",array)
print("Sorted array:\t",merge_sort(array))