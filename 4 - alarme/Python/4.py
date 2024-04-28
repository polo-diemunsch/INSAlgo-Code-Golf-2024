g=[*map(int,input().split(','))]
g[1]=12;g[2]=2
p=0
while g[p]!=99:
 if g[p]-1:g[g[p+3]]=g[g[p+1]]*g[g[p+2]]
 else:g[g[p+3]]=g[g[p+1]]+g[g[p+2]]
 p+=4
print(g[0])