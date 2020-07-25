Assignment 1

list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list2=list(list1)
a=0
for idx,num in enumerate(list2):
    if num==0:
        list2[idx]=110
def zero(z):
    global a
    i=list2[a]
    a+=1
    return i

list1.sort(key=zero)
print(list1)


Assignment 2(Method 1)

list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=[]
a=0
step=6
count=0
flag=True
while flag:
    if list1[a]<=list2[a]:
        i=list1[a]
        j=list2[a]
        list3.append(i)
        list3.append(j)
    else:
        i=list1[a]
        j=list2[a]
        list3.append(j)
        list3.append(i)
    a+=1
    count+=1
    if count==step:
        flag=False
print(list3)


Assignment 2(Method 2)


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=list1+list2
list4=[]
for i in range(0,len(list3)):
    list4.append(min(list3))
    list3.remove(min(list3))
print(list4)
    

