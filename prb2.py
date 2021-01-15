n1=0
n2=1
n=int(input())
print(n1,n2,end=" ")
sum=1
for i in range(1,n-1):
    sum+=n1
    n1=n2
    n2=sum
    print(sum,end=" ")