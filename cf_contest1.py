# Resu has been given the responsibility to sell handicrafts, made by people dwelling in the village. The money collected will be used to improve the condition of their village. Since the handicrafts are almost identical, Resu wants to sell each of them at a fixed price. Resu is going to visit N households where he can sell those handicrafts. Fortunately due to a recent survey, he knows mi which denotes the maximum amount of money which the ith household is ready to pay if they buy a handicraft. So Resu wants to know what is the maximum money he can collect considering that household will either buy one handicraft or not buy and the number of handicrafts he has initially is N .

# Can you help him figure out the maximum money he can collect ?


n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(n):
    l[i]=(n-i)*l[i]
print(max(l))
