import sys

with open(sys.argv[1],"r") as tdr:
	tdr = tdr.read().strip('\n')
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	tdr = "".join([complement[base] for base in tdr])
	print(tdr[::-1])
