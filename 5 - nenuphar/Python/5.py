g=[input()for i in range(350)]
q=[(0,0,"")]
v={0}
while q:
 i,j,p=q.pop(0)
 if(i,j)in v:continue
 v.add((i,j))
 if i+j==698:print(p[:-1]);break
 if j<349 and g[i][j+1]=='#':q.append((i,j+1,p+"R\n"))
 if g[i+1][j]=='#':q.append((i+1,j,p+"D\n"))