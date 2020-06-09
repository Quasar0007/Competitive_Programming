# Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to it's nearest space station.

# For example, there are n=3 cities and m=1 of them has a space station, city 1. They occur consecutively along a route. City 2 is 2-1=1 unit away and city 3 is 3-1=2 units away. City 1 is 0 units from its nearest space station as one is located there. The maximum distance is 2.


n,k=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
m=0
for i in range(k):
    if i+1<k:
        m=max((ar[i+1]-ar[i])//2,m)
    else:
        break
print(max(m,ar[0],n-1-ar[-1]))


# LOGIC:-The integer-half of the difference between two cities with space stations is the maximum distance for a non-space station city between the two space station cities and handling the conditions when 0th or last city is or isn't the city with space station. 