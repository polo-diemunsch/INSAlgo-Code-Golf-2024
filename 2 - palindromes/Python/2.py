from itertools import*
for s in product("abcdefghijklmnopqrstuvwxyz",repeat=5):
 if s==s[::-1]:print(*s,sep="")