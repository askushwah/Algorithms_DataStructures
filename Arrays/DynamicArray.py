# This program is used for the creation of Dynamic array. Though Python already has a list which is implemented using Dynamic array.
# In this, I implemented the dynamic array using list making them static and then increasing the capacity on the fly.
class DynamicArray:
    def __init__(self):
        self.arr = [0] * 4
        self.capacity = 4
        self.count = 0

    def add(self, num):
        if self.count < self.capacity:
            self.arr[self.count] = num
            self.count += 1
        else:
            self.capacity *= 2
            new_arr = [0] * self.capacity
            for i in range(len(self.arr)):
                new_arr[i] = self.arr[i]
            new_arr[self.count] = num
            self.count += 1
            self.arr = new_arr
    
    def remove(self, index_no):
        new_arr = [0] * (self.capacity-1)
        j=0
        for i in range(len(self.arr)):
            if i == index_no:
                pass
            else:
                new_arr[j] = self.arr[i]
                j += 1
        self.arr = new_arr
        self.capacity -= 1
        self.count -= 1
        print(self.arr)

    def print_arr(self):
        print(self.arr, len(self.arr))
    
    def get_index(self, index_no):
        if index_no < 0 or index_no >= len(self.arr):
            print("Out of bound error")
            return
        print(self.arr[index_no])

array = DynamicArray()
array.add(1)
array.add(2)
array.add(3)
array.add(4)
array.add(1)
array.add(1)
array.print_arr()
array.remove(1)
array.print_arr()
array.get_index(2)
