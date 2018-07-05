## Program to find the maximum sub array sum

class MaximumSubArray:
    def __init__(self, arr):
        self.arr = arr
        self.start_index = 0
        self.end_index = 0
        self.temp = 0
        self.max_so_far = 0
        self.max_end = 0

    # This is the famous algorithm to check for the max sub array
    # Start and end index keeps the track for the subarray indexes

    def Kadane_algo(self):
        for i in range(len(self.arr)):
            self.max_end += self.arr[i]
            # Check if the value so far that is added is greater and if yes, exchange
            if self.max_so_far < self.max_end:
                self.max_so_far = self.max_end
                self.start_index = self.temp
                self.end_index = i
            # If the value is less than 0, then convert the value to 0
            elif self.max_end < 0:
                self.max_end = 0
                self.temp = i+1
        return self.max_so_far, self.start_index, self.end_index

arr = [4,-3,-2,2,3,1,-2,-3,4,2,-6,-3,-1,3,1,2]
array = MaximumSubArray(arr)
result = array.Kadane_algo()
print("The maximum subarray sum is: ", result[0]," with starting index -> ", result[1], " and ending index -> ", result[2])

