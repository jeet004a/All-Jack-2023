#Longest substring in Leetcode
a=input("Enter your words:-")

l=list(map(str,a))
k=[]
c=1


for i in range(0,len(l)):
    p=[]
    c=1
    p.append(l[i])
    for j in range(i+1,len(l)):
        if l[i]!=l[j]:
            if l[j] not in p:
                p.append(l[j])
            else: 
                break
        else: 
            break
        if l[i]==l[j]:
            break
    k.append(len(p))
print(k)
