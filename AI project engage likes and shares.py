posts=[{"title":"ML","likes":10,"shares":12,"No":"01"},{"title":"NLP","likes":20,"shares":10,"No":"02"},{"title":"AI","likes":50,"shares":102,"No":"03"}]
# a=dict(posts[0])
# print(posts[1]["likes"])
x=len(posts)
y=0
lis=[]
while(y<x):
    a=posts[y]["likes"]+posts[y]["shares"]
    y=y+1
    lis.append(a)
print(posts)    
print(f"{posts[2]["title"]}'s highest engagement = ",max(lis))


     


