import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 k=0
 while k<n and a[k]==1:
  k+=1
 if k==n:
  print("First" if k%2 else "Second")
 else:
  print("First" if k%2==0 else "Second")