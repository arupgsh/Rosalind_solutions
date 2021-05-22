import sys

#data = open(sys.argv[1],"r").readline().strip("\n").split(" ")
#inp = ','.join(data)
#print(inp)
def rab(n,k):
	if n == 0 or n == 1:
		return n
	else:
		return rab(n-1,k) + k*rab(n-2,k)

#print(rab(5,3))
print(rab(28,5))
