# Maxim wants to buy an apartment in a new house at Line Avenue of Metropolis. The house has n apartments that are numbered from 1 to n and are arranged in a row. Two apartments are adjacent if their indices differ by 1. Some of the apartments can already be inhabited, others are available for sale.

# Maxim often visits his neighbors, so apartment is good for him if it is available for sale and there is at least one already inhabited apartment adjacent to it. Maxim knows that there are exactly k already inhabited apartments, but he doesn't know their indices yet.

# Find out what could be the minimum possible and the maximum possible number of apartments that are good for Maxim.

# Input
# The only line of the input contains two integers: n and k (1 ≤ n ≤ 109, 0 ≤ k ≤ n).

# Output
# Print the minimum possible and the maximum possible number of apartments good for Maxim.

n,k=map(int,input().split())
if k==n or k==0:
    print(0,0)
else:
    print(1,min(2*k,n-k))