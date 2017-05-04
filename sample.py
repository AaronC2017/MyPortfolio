s = "1100010" 
v=0
i=0
while i < len(s):
   v = v * 2 + int(s[i])
   i=i+1

print v