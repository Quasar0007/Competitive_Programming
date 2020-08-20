# There are a number of plants in a garden. Each of these plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.

# You are given the initial values of the pesticide in each of the plants. Print the number of days after which no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their left.

# For example, pesticide levels p=[3,6,2,7,5] . Using a 1-indexed array, day 1 plants 2 and 4 die leaving p=[3,2,5]. On day 2, plant 3 of the current array dies leaving p=[3,2]. As there is no plant with a higher concentration of pesticide than the one to its left, plants stop dying after day 2.

def poisonousPlants(p): 
    inf, ans = float('inf' ), 0 
    stack = [[-inf, inf, inf]] 
    for i in p:
        while stack[-1][0] >= i or stack[-1][1] - stack[-1][2] == 0:
            stack.pop() 
        if i > stack[-1][0] and stack[-1][0] != -inf:
            stack[-1][1] += 1 
            ans = max(ans, stack[-1][1])
        stack.append([i, 0, stack[-1][1]] ) 
    return ans
n=int(input())
print(poisonousPlants(list(map(int,input().split()))))

