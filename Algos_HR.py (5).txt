*****Madison, is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory . Mason has a 2D board A of size H*W with H rows and W columns. The board is divided into cells of size 1*1 with each cell indicated by it's coordinate (i,j). The cell (i,j) has an integer A-ij written on it. To create the toy Mason stacks A-ij number of cubes of size 1*1*1 on the cell (i,j).
Given the description of the board showing the values of A-ij and that the price of the toy is equal to the 3d surface area find the price of the toy.


==>n,m=map(int,input().split())
l=[]
s=2*n*m
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(len(l)):
    s+=(l[i][0]+l[i][-1])
    for j in range(len(l[i])-1):
        s+=(abs(l[i][j+1]-l[i][j]))
l=list(zip(*l))
for i in range(len(l)):
    s+=(l[i][0]+l[i][-1])
    for j in range(len(l[i])-1):
        s+=(abs(l[i][j+1]-l[i][j]))
print(s)
    


LOGIC:-2*n*m denotes the top and bottom surface of the toy.The next "for" loop is for the left and right surface area of the toy,whereas the last two "for" loops are for the front and rear surface areas.