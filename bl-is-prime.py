import sys
number = sys.argv[1]
#Convert value to a number
n = int(number)
j =2
while j < n and n % j != 0:
	j = j + 1
print j == n