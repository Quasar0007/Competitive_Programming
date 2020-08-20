# Task
# Write a Calculator class with a single method: int power(int,int). The power method takes two integers,n and p, as parameters and returns the integer result of n**p. If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

# Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.


Exception="n and p should be non-negative"
class Calculator:
    def __init__(self):
        return 
    def power(self,a,b):
        if a>=0 and b>=0:
            return a**b
        else:
            return Exception
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   