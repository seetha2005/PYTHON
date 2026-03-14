
x=int(input("Enter amount in Rs:"))
coins=[500,200,100,50,20,10,5,2,1]
for i in coins:
    while i<=x:
        print(i,end=" ")
        x=x-i

