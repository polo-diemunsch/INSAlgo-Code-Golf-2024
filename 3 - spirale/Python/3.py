d=lambda x:print("  "if x else"[]",end="")
for i in range(-8,10):
 for j in range(-8,10):
  if j<=0:d((j<-abs(i)or i%2)&(j%2 or i>abs(j)or-abs(j)>i))
  elif i<0:d((j>abs(i)or i%2)&(j%2==0 or-abs(j)>=i))
  else:d((i%2 or j>=i)&(j%2==0 or i>j+1))
 print()