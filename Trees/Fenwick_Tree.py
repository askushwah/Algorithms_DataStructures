# Fenwick trees is basically used for querying range queries in the list
# Fenwick trees are also called as Index Binary Trees and they overcome the so called limitation of calculation using prefix sum array.
# The time complexity is log time but the only requisite is that the size of the array should be fixed.
import copy
class FenwickTree:
    def __init__(self, arr):
        print(arr)
        self.arr = arr
    
    def PrefixSum(self, num):
        result = 0
        while num > 0:
            result += self.arr[num-1]
            num -= self.LSB(num)
        return result

    # Calculating least significant bit of a number
    def LSB(self, num):
        return num & -num
    
    def Subarray_sum (self, num1, num2):
        print("Subarray Sum between index %d and %d is : %d " %(num1, num2, (self.PrefixSum(num2) - self.PrefixSum(num1-1))))

    # Instead of making a seperate copy of the array, I am updating it in the same array.
    # This has a limitation as it changes the original array
    # we can use copy.deepcody to make a new array and construct the fenwick tree into that array   
    def TreeConstruction(self):
        for i in range(1,len(self.arr)):
            j = i + self.LSB(i)
            if j < len(self.arr):
                self.arr[j] += self.arr[i]
        print(self.arr)
        return self.arr

arr = []
for i in range(0,13):
    arr.append(i)
tree = FenwickTree(arr)
num1 = 5
num2 = 7
tree.TreeConstruction()
tree.Subarray_sum(num1, num2)
