import sys

gc_dict = {}
with open(sys.argv[1],"r") as tdr:
	tdr = tdr.read()
	blocks = tdr.split(">")
	blocks.pop(0)
	for block in blocks:
		line = block.split("\n")
		id = line[0]
		seq = line[1:]
		seq = ''.join(seq)
		gc = seq.count("G")+seq.count("C")
		gc_pct = (gc/len(seq))*100
		gc_dict[id] = gc_pct
		#print(gc_pct)
		#if gc_pct > max_gc:
		#	max_gc = gc_pct
		#	seq_id = id
max_gc = max(gc_dict, key=gc_dict.get)
print("{}\n{}".format(max_gc,gc_dict[max_gc]))
