class KMP_Algo:
    def __init__(self, string, pattern):
        self.string = list(string)
        self.pattern = list(pattern)
        self.prefix_arr = [0] * len(self.pattern)

    #Create and LPS array to find the preffix array of the pattern, substring, etc
    def LPS(self):
        j = 0
        self.prefix_arr[0] = 0
        i = 1
        while i < len(self.pattern):
            if self.pattern[i] == self.pattern[j]:
                self.prefix_arr[i] = j+1
                j+=1
                i+=1
            else:
                if j != 0:
                    j = self.prefix_arr[j-1]
                else:
                    self.prefix_arr[i] = 0
                    i += 1
    
    # KMP algorithm to check the pattern in the string
    def KMP(self):
        pattern_index = 0
        text_index = 0
        flag = 0

        while text_index < len(self.string):
            if self.string[text_index] == self.pattern[pattern_index]:
                pattern_index += 1
                text_index += 1
                if pattern_index == len(self.pattern):
                    print("Matching pattern found")
                    flag = 1
                    pattern_index = self.prefix_arr[pattern_index-1]
            else:
                if pattern_index != 0:
                    pattern_index = self.prefix_arr[pattern_index-1]
                else:
                    text_index += 1
        if flag == 0:
            print("There was no match of pattern string in the given text string")

    

string = "AAAAAAAAAB"
pattern = "AAA"
algo = KMP_Algo(string, pattern)
algo.LPS()
algo.KMP()
