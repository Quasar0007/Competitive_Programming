# It's Lolympics 2016 right now, and we all know who's the best player there right now: Kalyani! Obviously, he has a huge female fan following and he has to make sure they are all happy and rooting for him to win the gold medals.
# But with fan following comes arrogance and lack of time. Thus, he has sufficient time to interact with atmost T of his fans. Each fan is defined by two parameters : Name and Fan Quotient. The name defines the name of the fan, while the fan quotient is a measure of the fan's devotion towards Kalyani. Higher the fan quotient, greater is the devotion. Kalyani now wants to meet T of his fans. While selecting the fans he wants to meet, he wants to make sure that a fan with a higher fan quotient should be given a chance in favour of those with lesser fan quotient. In case of ties, he sorts their name lexicographically and chooses the lexicographically lesser named fan.
# Given details of N fans, can you help out Kalyani by giving him a list of fans he would be interacting with?


n,t=map(int,input().split())
d={}
for _ in range(n):
    name,quotient=map(str,input().split())
    quotient=int(quotient)
    if quotient not in d:
        d[quotient]=[name]
    else:
        d[quotient].append(name)
        d[quotient].sort()
l=[]    
for i in d.keys():
    l.append(i)
l=sorted(l,reverse=True)
ct=0
for i in l:
    while len(d[i])>0:
        print(d[i][0]) 
        del(d[i][0])
        ct+=1
        if ct==t:
            break
    if ct==t:
        break