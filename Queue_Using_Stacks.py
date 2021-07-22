def Push(x,stack1,stack2):
    stack2.append(x)
    return stack2
    #code here

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    if stack2==[]:
        return -1
    else:
        return stack2.pop(0)