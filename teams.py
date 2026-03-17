import random
n=int(input("Enter num of teams:"))
teams=[]
for i in range (n):
     x=input("Enter teams:")
     teams.append(x)
meet=int(input("Enter num of meeting by two teams:"))
matches=[]
for i in range(n-1):
    for i in range(i+1,n):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffles(matches)
pos=1
for i in matches:
    print("matches{}:{}vs()".format(pos,i[0],i[i]))
    pos=pos+1
 
 
 