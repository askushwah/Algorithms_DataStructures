class PriorityQueue:
    def __init__(self, arr = []):
        self.arr = arr
    # Get index of the respective nodes
    def getRightChildNode(self, parentIndex):
        return (2*parentIndex) + 2
    def getLeftChildNode(self, parentIndex):
        return (2*parentIndex) + 1
    def getParentNode(self, childIndex):
        return int((childIndex-1)/2)

    # Check if there exists a node or not 
    def hasRightChild(self,index):
        return self.getRightChildNode(index) < len(self.arr)
    def hasLeftChild(self,index):
        return self.getLeftChildNode(index) < len(self.arr)
    def hasParent(self,index):
        return self.getParentNode(index) >= 0
    
    def rightChild(self, index):
        return self.arr[self.getRightChildNode(index)]
    def leftChild(self, index):
        return self.arr[self.getRightChildNode(index)]
    def parentIndex(self, index):
        return self.arr[self.getParentNode(index)]
    
    def swap(self, num1, num2):
        print(self.arr[num1], self.arr[num2])
        self.arr[num1], self.arr[num2] = self.arr[num2], self.arr[num1]

    # Return the first element from the heap
    def peek(self):
        if len(self.arr) > 0:
            return self.arr[0]
        else:
            return "Array is empty"

    # Remove the first element from the heap
    def poll(self):
        if len(self.arr) > 0:
            item = self.arr.pop(0)
            self.heapifyDown()
            return item
        else:
            return "Array is empty"
    
    # Add the value and heapify
    def add(self, value):
        self.arr.append(value)
        self.heapifyUp()
    
    def printQueue(self):
        print(self.arr)

    # Check if the heap invariant is staisfied after adding the value
    def heapifyUp(self):
        index = len(self.arr) - 1
        while self.hasParent(index) and self.parentIndex(index) > self.arr[index]:
            print("Parent", self.parentIndex(index))
            self.swap(index, self.getParentNode(index))
            index = self.getParentNode(index)
    # Check if the heap invariant is staisfied after removing the value
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChild = self.getLeftChildNode(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChild = self.getRightChildNode(index)
            if self.arr[index] < self.arr[smallerChild]:
                break
            else:
                self.swap(index, smallerChild)
            index = smallerChild

# li = [5, 7, 9, 1, 3]
heap = PriorityQueue()
heap.add(5)
heap.add(7)
heap.add(9)
heap.add(1)
heap.add(3)
print(heap.poll())
heap.printQueue()
