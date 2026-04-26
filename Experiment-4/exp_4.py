t=int(input())
for _ in range(t):
 n=int(input())
 if n==2:
  print(-1)
  continue
 a=[i for i in range(1,n*n+1,2)]+[i for i in range(2,n*n+1,2)]
 for i in range(n):
  print(*a[i*n:(i+1)*n])