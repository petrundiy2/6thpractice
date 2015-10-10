N=int(input())
A=list(map(int, input().split()))
k=0
for x in range(N):
    if A[x]>5:
        k+=(A[x]//5)-1
    if A[x]==5:
        for y in range(x,len(A)):
            if A[y]>5:
                k-=1
                break
if A[0]>5 and k<=(A[0]//5)-1:
    k=(A[0]//5)-1
if k<0:
    print(0)
if k>=0:
    print(k)
