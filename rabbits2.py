def rab(n,k):
	if n <= 2:
		return n
	else:
		return rab(n-1,k) + k*rab(n-2,k)

#print(rab(5,3))
print(rab(6,3))
