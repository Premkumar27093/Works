t=int(input())
s=[]
def values(s,n):
    return print(s[0:n:2], s[1:n:2])
for i in range(0,t):
    s=str(input())
    n= len(s)
    values(s,n)
