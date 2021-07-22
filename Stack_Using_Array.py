class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
        #add code here
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if self.arr!=[]:
            c= self.arr[-1]
            del(self.arr[-1])
            return c
        else:
            return -1