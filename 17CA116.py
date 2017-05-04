#Question 3a

a = [4,10,1,7]
i = 0
curr = 0
while i < len(a):
	curr = a[i] + curr
	i = i + 1
print curr