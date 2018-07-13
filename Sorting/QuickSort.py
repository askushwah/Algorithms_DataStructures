# Quick sort using an auxilary array
# Reference: https://www.youtube.com/watch?v=1Mx5pEeTp3A&list=PLEJyjB1oGzx2h88Tj90B5_HadLq339Cso&index=10
from random import randint
def create_array(size = 10, max_size = 50):
    return [randint(0,max_size) for _ in range(size)]

def quick_sort(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [],[],[]
    pivot = a[randint(0, len(a)-1)]

    for x in a:
        if x < pivot: smaller.append(x)
        elif x > pivot: larger.append(x)
        else: equal.append(x)
    return quick_sort(smaller)+equal+quick_sort(larger)
array = create_array()
print("Unsorted array:\t", array)
print("Sorted Array:\t", quick_sort(array))
