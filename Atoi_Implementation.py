class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        
        for i in range(len(string)):
            if not string[i].isnumeric():
                if i==0 and string[i]=="-":
                    continue
                else:
                    return -1
        return int(string)