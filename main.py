def data_insert(list,data,position):
    list.append(None)
    for i in range(len(list),position,-1):
        list[i-1]=list[i-2]
    list[position]=data

friends=[('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]

friend=input("추가할 친구-->")

count=int(input("카톡 횟수--->"))
k=0
for i in range(len(friends)):
    if friends[i][1]>count:
        k+=1

data_insert(friends,(friend,count),k)

print(friends)
