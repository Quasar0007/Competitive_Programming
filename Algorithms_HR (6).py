# You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge.
# Find all the cavities on the map and replace their depths with the uppercase character X.
# For example, given a matrix:

# 989
# 191
# 111
# You should return:

# 989
# 1X1
# 111
# The center cell was deeper than those on its edges: [8,1,1,1]. The deep cells in the top two corners don't share an edge with the center cell.



n=int(input())
l=[]
for i in range(n):
    l.append(list(input()))
for i in range(1,n-1):
    j=1
    while j<n-1:
        if int(l[i][j])>max(int(l[i][j+1]),int(l[i][j-1]),int(l[i+1][j]),int(l[i-1][j])):
            l[i][j]="90"
            j+=2
        else:
            j+=1
for k in range(n):
    a=''.join(l[k])
    print(a.replace("90","X"))




    
# LOGIC:-Identify the cavity element and replace it with a large number so that the numbers on its edges never exceed that number .Finally ,replace that large number with 'X' and print the string.