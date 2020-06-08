*****Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.
There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by h[i] where i belongs to [1,n]. If you join k adjacent buildings, they will form a solid rectangle of area k*min(h[i],h[i+1],....,h[i+k-1]).
For example, the heights array h=[3,2,3]. A rectangle of height h=2 and length k=3 can be constructed within the boundaries. The area formed is h*k=2*3=6.


==>n=int(input())
h=list(map(int,input().split()))
m=0
for i in range(n):
    j=i+1
    l=i-1
    while j<n:
        if h[j]>=h[i]:
            j+=1
        else:
            break
    while l>=0:
        if h[l]>=h[i]:
            l-=1
        else:
            break
    m=max(m,(j-l-1)*h[i])
print(m)


LOGIC:-Select all the buildings before and after a particular building having height equal to or greater than the current building and take out the area and check if its the maximum and update the maximum as per after every iteration of the building.