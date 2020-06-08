*****Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the minimum number of elements to delete to reach his goal.

For example, if his array is arr=[1,2,2,3], we see that he can delete the 2 elements 1 and 3 leaving arr=[2,2]. He could also delete both twos and either the 1 or the 3, but that would take 3 deletions. The minimum number of deletions is 2.


==>from collections import Counter
n=int(input())
l=list(map(int,input().split()))
a=Counter(l).most_common(1)
print(n-a[0][1])


LOGIC:-Using the Counter module ,we take out the no.of times that the most common element in the list appears ,so we need to delete the remaining number of elements in the list.