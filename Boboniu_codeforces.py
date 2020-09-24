# Boboniu gives you

# r red balls,
# g green balls,
# b blue balls,
# w white balls.
# He allows you to do the following operation as many times as you want:

# Pick a red ball, a green ball, and a blue ball and then change their color to white.
# You should answer if it's possible to arrange all the balls into a palindrome after several (possibly zero) number of described operations.


t=int(input())
for _ in range(t):
	r,g,b,w=map(int,input().split())
	if (r%2+g%2+b%2+w%2)<=1 or (r%2+g%2+b%2+w%2)==4:
		print("Yes")
	elif (r%2+g%2+b%2+w%2)==3 and r>=1 and g>=1 and b>=1:
		print("Yes")
	else:
		print("No")
