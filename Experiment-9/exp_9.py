import sys
input=sys.stdin.readline
n=int(input())
edges=[tuple(map(int,input().split())) for _ in range(n-1)]
g=[[] for _ in range(n+1)]
for i,(u,v) in enumerate(edges):
 g[u].append((v,i))
 g[v].append((u,i))
ans=[-1]*(n-1)
cur=0
for i in range(1,n+1):
 if len(g[i])>=3:
  for j in range(3):
   ans[g[i][j][1]]=cur
   cur+=1
  break
for i in range(n-1):
 if ans[i]==-1:
  ans[i]=cur
  cur+=1
print(*ans)