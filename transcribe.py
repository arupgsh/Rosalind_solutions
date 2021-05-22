import sys

with open(sys.argv[1],"r") as tdr:
	tdr = tdr.read()
	tdr = tdr.replace("T","U")
	print(tdr)
