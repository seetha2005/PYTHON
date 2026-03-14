name=['GILL','ABI','RAHUL','JOHN','ANU']
age=[23,45,67,32,20]
loc=['chennai','Trichy','Pondy','Salem','Chennai']
res=list(zip(age,name,loc))
res2=sorted(res)
for i in range(5):
    print("{}.{} age is {} lives in {}".format(i+1,res[i][1],res2[i][0],res2[i][2]))