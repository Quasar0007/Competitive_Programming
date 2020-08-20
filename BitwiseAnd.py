# Task
# Given set S={1,2,3,....N}. Find two integers,A and B (where A<B), from set S such that the value of A&B is the maximum possible and also less than a given integer,K. In this case,& represents the bitwise AND operator.


T = int(input())
for _ in range(T):
    n , k = map(int , input().split())
    print(k-1 if ((k-1) | k) <= n else k-2)