#best way to generate codon table: https://github.com/ixaxaar/rosalind/blob/master/Translating%20RNA%20into%20Protein.py
bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

test='AUGGUCAUGUGCCGAUGUUGCAUGCCUAUGCUGCGGCGAGUUAAAAGAAGGGGUCGAUGCUUACCCAACGCCCAAGAGCAUAUAAGGAGCACGCGUGCCCGCGGCUGGUCCCGUUACUUCAAUCGAGUCCUGUUUGCCGGGCGGUGUCCUAAAUGCGGGCGACUCGAAAUUCUUUGGGAUACUACACGCGUGUGUAAGCGUCAGUAUCAUACAAAUAAUAAUAAACGCUUGGUUAAUUUCAAAGUUCUCGGUUUGGUUUUUUCUUGUUCCGUAAGGGGAUUCACUACAAGGACAAUACAAGCAACAGUUUCACUGUCCCACCUCAUUGCACGUGAGAGAAAUUCAUAUAACAACUCGCCGGCGGGUGAUAUUCAACUGGCACUGAUGCUUCUAAGCUGCAAUAAGCCUAAUCGUCUCACGAUCUCAAUUCCAUUCAAUGACAAAGGUAUCCAGUAUGUGUCAGUCCUCGCCGCGCUAGCGGAAAUAGUUGACACCGGAGCUCGAUUUCCCACGCACGCGAGGAUACAUGCACAUUACCCGAAGACGCACCGGCUGCUAGGUCAACGUAUAGAAGGCACCACCGAAACCGGGGCAGCUCGUUUCCGAGCUCUCUCGCAACAUAUUUGCUCACUUUCGUGGAAGUUACGACAAGUUGGGUCCAAGCGCGGAAAAGCCAUUCCGCAAGAGCUCCCUAGGCCCUGGUGUGGCUACCGGUCGCACAUUGUAAUAUGCAAGCAGGGUUAUGAUCCUAGAAAUUUACAACACGAGGCCCUCGUGUGUAGAAGCCGUCCGAAGCAGCUGAACGCUCCAACGAUACAAAGCGACUAUCCUAUAAUAGCCCCCCGCGCAUGUAACAAUAUGGUUGAUGUCGCAUGGCGGAAUCGUUUCAAACUUUAUCCCCCCUAUGACUUAGUUAGGAUGGAUUGUGACUCAUGGCUAAAGUGUGAGCCCGUAUGGGGGAACAACAUGGGACCCCUUUCGCCACAGAUGACGGUUAGGGGCCACUCGCCUAAAGUUAUUUUAGCGGUUCCCGCCACGUUAGCCGCCGCUCUAGAGGUAAAGCGCGGAUUUCGGUGUAGGGCAUCGCCUAUUAAAUGCUCAGCUGACGAUAGGAUGAGUGAUGGAUGGGUGACUGGUCUUCGUAUUUCGGGAAUUCGCCUAUUCCUAGGACGUUCACUCUGUGGUAUGCAAGAGCAACAGGAAGAGUGCCCAAAUUGUUGGCGCAAUUAUGACACGUACCCUAUACUUAGAGCAUUUAAUCAUUCGACCCGUGAAAACCUCAAGCGCGGUUCUAAAACCCCCCGUCGGACGAAGCUUACGUGCAUAAGGGCGUUACGGCUUAGGCCUCAGUUGCUUUAUUGGGUAGCCUUUACCAUCGUAACAGUCCCGGGAAUGUCUAGCCGCACGGUGCGUAAGGUAAGCCAGUCGAGAAUUCAUCGAACCACGGAGUCUUCUACGGCCCAGGGAACUCAUCGCACGGUCUAUAGAACUGUCGUGCUCGAAUUAUUAAGCUGCUCUCCGCCCGACGUAAAUUUAAUCUCGAACGAUAGCUGCGCAGGCCAAGAUUUGCUGCCGCCAUCUACUCUAAUAGUUAGCAGGAUCAUUCAACCUGUCCUGGUACAGUUAAGAUUCAGUUCAGAUACGAACAGCCGCGAUUUAAAUCUUUACCCACCAGGCUUGGGGCAUCCUGGCUCACGAGCCUUUCGCCGACUUGAAACCUCCAUACAACGCCUGGGGCUCCGUUUGAGAAAGUUUGCCGCUCAUUACUCCCGUACAUGUCUGCAUAUAGUCGAUUGUACACUGGCGCACUGUCGCGCAUGGUCUUUUGAACACCAGCACUACAGCUCACGGACUCCGCUAUCUUCCCGCUAUACAUCUCCUAUCCGGUUUGUGCCGUGGCCAAAUUUCGAUGCGAACGGCUUCCUAAAGACUGCAGCACCCCUGAGCCUAAAAAGGAUCCCAAACCAGGAGGUCGAGUCGAAUGGGGAGAAAAAGCUCGGAGGGCUACGGUGUUCGCCUGCAUUGGGGACGUGUAACGAACUAGCUGUGACUGGUGCAACUCGUCACAUCUUCGCCCCCCCCACCGUGUUUUCAACCAGUUAUUUCUCGCCACCCGCACUAUCGAAAGCGAUGAAAAAGACGAUAAAAUCCGAUUUGGAGUAUAGCAGUCUUAGCAUCAACGUAUAUAAAGACUGUGAUGCCCAUUCAUCUCUGGGAGUUUACUUAACUGGCGACGCGAUAUCUGGAAUAUCAUACAGCAUCUGCUUCAGAGGGCAGCAUAGGUUAGCCAUUACAUCACUAUAUUUAGAGCUCGUAUCCACAUCCAGCGUUGGAAAUGCCGCUCGAUCGCCCUCAAAUUCCUACAUCCGUGUACUACUUGGAUCAGGUGCUCGCGUAUACACUCUACAGCUUGUUAUACGAAAAACAUUGAGUCUUGAACCGCUAAGCUUAUUAAAACGUCAACGUUGGCUACUAAUUAGAGUCGCGCACCGAGCAUCGUAUGUAUCCGAACUCGAGAGCCAAUUAACCAUCGAAUUGAUAGCCUGGACGGGUAUUCGGAGUUGGUUGAAAAAUACGCAGAUUAUGUGGUGUGAUUUCAUCCUACCAUCGGGUCACUACACAAGAUUCAGCGUACUUGAAAGGAUGUGUGAAUCAGUUCGUUCUGACAACCUAUAUCGUUCCCUUUCUAACACCCUCGGUAUUAAUUUUACCGCGAAGGGAAAUAUCAGGUGGCAUUCCCGCCGCUCUUUAUGGAUUAAGAUGGAUAGUGUUCGACAGUUGUUCGCUAAUACUUUAGUAUCACGGUUUCUGCGAAGGUAUAGGGACGUAGGUACUGAAACUCCUAAGACAAAUGUCAUCGUACACAUAUCGAACUGGGUCAGCUGGCUAUCGCAUCCCUCAAUCGAUCGUAGUUUGGGGGCAAUCUCGGAGAGAGAGCGGCGCAUGGCGUGGACACUGUACAACGAGCCACGUUUGGAAUGGCCACUCAGGACCCGCAGCCACAUGGGUGUCGUGCCACACGCCUUCUUGACGAAAGAACCGAUAUCGGCUCUGAGUAAACCUACUGUGGGAUCGUUGCCAAUUCACCACCGGCGGCAUGCCAAUGACAUGAAAUGGACCGAGCUUUCUUAUACCUCGUCGGGGUACGCCGGGCAAGCUAGAUCACCUACACGCUUUUGGAAUAACUGUCGGCGCCUAAAAACUCCCUUAGAGUCCUUAUCAUGCUACUUACGACAGUCAUCUUGUAAUGGCAUAAACUCUGACAAGGCUUCAAAUCAGGCACCUUACCGAUCUACAGUGAAUCUCGUUUGUAGAGCAGUAGGUCAAGUUCUCAAAAUACUUGAUGAGUGCGCAUUAGACAAGUGCCUUACCUUGGGGUCUUGCCCUUGCAUCGACUAUGCGUGGCAAGGCAUUCGAGCGGAUAAUCCAAUCACUGGGUGGAUACACCCUGAGAAAUCUUAUCAGGGCUCCGGUGAACCGUUACAGGUACGUCUGAGUGAGAACAGUCACUGGCUGCGAGUCUUCCCCGGAAUCCGUCUAUUGGACGCGAUCCUUAUGACCGAACAAGGUCAUUCCCAAGGCUUAGUAUUUGCAAUUUCAGAGGUUCGAAUUACCAACGAGCGCGCUCCUCUCAUACACAGAGAGGCCAUGCUCCCGCCACGCCUUCAAAAGCUUGGUGAUACCCAUUGUAGGCCUCGGGUCUCCACAAGUUCCCUUAAGUGUCUGCACGCAGCACGAAUGCGGUUCGUAGGUAUACGCCUCGAGCAGAGCAUGCCUCAGCAGAGAGUCGACCGAUUGCAUAUUUCGCACUUACGAUUUUCACGAAAAAAUGGCAGCUGGGGACAUCAGCAGGGCCACUGGAGAGACCAAAUCUUGGAUUUGGCACGCGCGGCAGAGUGUAUAUUAACGGGCGUCCAGGUUAUAUUCAUGCACUCACUCCCGUGUAGUAUUGUACCCUACGGGUAUUGGUGUCCCCGACCGUUGUCAAGGCAUUAUUCAUCGCGUGGCCUGGCUUAUACUUGUCUCUAUAUAUGCCACGGUUCCCUCUCCAUGGGCCUUCCGCAAAAGGCGGUGAUAGUAGGGCCAGUUAGUCGGCUAGCUUUCGGGACUACGUGCAAAUCGCCCUGUCGGUCAUAUCGAGUUAGUCUGGUAGAGUGGUUCAAAGUGCUGGUGAUUCCCAUACGCGAGAGGGCCAGGAGUCCGUUAUCCUCCUCUUGUCGCGGAUCAAGUCCGCAAUGUGUAAACGAGCGCGAUCCUCUAGAAGGACGGCAGAAAACUUAUCUCACGCGCCUACGGAAAUGCGAAACCAUAGGGGAGGUAACCCCUUUUAAGUUUGUAUUGAACAUGGCCGGUCCCCCGACAUAUGGACUAAUCGGUGCGCGUCAAAGUAUGCGGACAUUGAUUCUUUGUUUGUCUGUAUUCCGACCCGAUCCUAAAACAACCAGGGCGAUCUCAAACCAGGGGAAACUGCUUUGCACAAACGCACCUAUUUGCUUCCCGCCAGCGCUCACGGAAGUGAGGUACGCGAGCAGCCACUACGGCCCACUAGGUUGUGACCGGGUGUCUGGGAACUAUCUGUCCCUGGCAAUAGCUGGCAGACACCCCAGGGUGGAUCCACUUACCACAGCAGGUGUAGUCCCUGACAGGAAUCCAUUUUUCCCCAACAGUGGGCGGAUCGGCGCCUCUGGCCAAAAGUCUACCUUCCUCGGAAUAUGGGAGCACUCGUAUGGCUAUUUUGGUCCUUUAUAUGUGCUGCCUUGGCUAAACCAUCGAUUAAUGCCGGCUCGGAUGGGGCAUCCCGACCCCUACUCUUGGACGGCAGUAGGAAGUCAAUACAGUUCGAGGGCGUACAAUGAUUUUGGGGGUCGCCCGCUCGGAUUGGCUGACGCGGAAGUCUAUCCAUUUCCCUCUCGUCCUCAUCGUUACAUGAGUACUGCGGAAACACGGGACCGACUCUGGAUCUCUUGCAGACUCGGAGACAAGACGACGGGGAAAAUCUCCCUUUUCCAGUACGCGAGCUGCUUCUGUAAUGGUAAGAGCCGUAGCGUGAGCCUUCGCUUACUCGCGAUUAGCACCAGAGCAGGCGCUGCCGGAGCACUAUCGACGAAGGGAAUAUUAACUUCAAGACAGGUCCGCCCAUUUCACACGCCGCAAUGUAACCACCACCCCUAUCGGAUCAGCUUUUUUAAGUCCAAUAUUUCGAUACAUCUCGAGUGUUUCGACGGACGAUUCCUAUGUACGGUAUUCUGCGAGUUAAAGUCAAUAGGCCUGGUACCUCCGUUUAUUGAUUGGGUUGUAGAGACCAUGUUAACGAUCAUUAGCGCUGAAUAUUUUGAAAUUGGUGAGAAACCAAACCCCAGGCCCGUCCCAACGACCGUCGUAACCUAUCUUCUAAAGUCAGUAAUGGGAGGUUGCAGGGAUCUUCGCGAAAACGCGUUAGCCUCGCUUAGAAGGCGCGCCCGUAUCCCCAUGCAACUACGGAUCACACAGAUCCUUUCCACGACAAGCUUUGAGAGGAACAUAGAUGCACGGAACACGCACGAGACGUUUCGGGUCACUUGCUCGAAUCUGGGUUUGCUUGGUCCAAAAUUCUGUGGCACAUGUCCACAUCCCCUUGUAGGACCCUCACUUUGUAAGGAACUGCGUCAUCUCGUCCCGGCCUGUGCGACCUUACAGAGGUCUGCAAAAUACGUGGUAGCGGUUCGAACAACCCCAUCGCUAUGGAGAGUACAGGAGUUUGUAACAUUAAUCGUGGGAACGCGAGACGGACGACGCGGGGACAUUUCGGCCAAGUGUGAACUACAUGCCUGCAUCAACGCAUCACACGUACCCAAGACUGGAAUAACGUCGUUGAGGCCUCUCCCGCGCGGCUUGGGGUGGGCAGAAUCAUUGCGAGAGGCCGCGAAUAAUGGCGUGGCGCCAAGGGGCAAGCCCGCGCUAGGAACAUCAGUCCGGAAGGUGGAAGACCAGCCCCAACUCAAGCAUACUCAGCGAACCCUCUACGUUGCUGGGUCUCUCUGUGUAGAUACAAAGCCUGGGUUUGGUGUCUCCGGUACCGUCCUUUUGAAGCGGCGUAUUCCCACACGCAUUCCUCAUCGCCCCUGUGCAGACUUGAAAACGCGUUAUGCUUACGAGAACCAAGAGACACAUUUUGCGGUCCUAGACACCGACUGUCCUACUUCUUUAUGUGCAUACGCUACUCUUCAGUACACCGAAAAUGCCAUCCAGAAACACAUCGGAGUCGUAGCAACACGCGGACACGGCGGGCAAACGAUCCACUGUGUGUCGCAAUCACUGGGUUAUGAUAGCGCGACUCACCACAUUACCUACCAAAGGCUGUGUAACGAGCACUUUUUAAAACCUCGAGACCGACUGGCGGAUCCACCCUUGAGACUACCAGGACAAGUUGCAGUACGAUACUCGAAAGGGGCGCGCGCUCCGGGCCAGGUAACAGGCUCCCGGAGGACGAUUGGGCAGGUGCCCGAUUGGUUACAAUGUCAUGAUGGCCGGGCCGUGGCUUCGUCUUUAUCUGAUACGGACACCCCGGGGCAGUCAGGUGGGGCACAAUAUGCUAACAGGAUUCUCAAUGAUUGGGCUACUGCCGAAUAUCUUCCAGAUAAAAUUUGUCUGGUUGAUAAGGAUCGCGCUUCGGCUCUGAGCAAUAAUAAGGCAUUUCCAGAAGCUCUCAUUUUGUCUGUAAGGAUCGGCAUAGGUCGGCAAAGAGGUACAUUUCUGGUGAUGUCGACGUCUUCCCACUGGGAACUGGUUCGUCUCUGCACCACCAGAGUACGGAGAUUCGGCGCUAUGACUAACACAAUCGCGUUGUUGAUGCCUAGUUCAGUGAGAGGCAGACGAUCGCAUGCUCUAUUCAGUUGUACCGCUAGAGAGCGGUGUGCUUGCUCCUGUUACGAAGGAAUGUAUAGAGACAGGCUAUUAGGGAAACAAGGAUGCAACAAAGGAACAAUAUUAUUGCAGUUGCCCAUACUGCUGGAAGUUAAAGCUACUCGCACCCAUGCUGAGGGCCAGAGGGAGGUCAUCGUUAACGAAGCCUCGUUCGCGAACCCGACUCAUUACCUAACCUUGGUGGUCCGGUCAAUUACUCAAUAUAGUGUCACCGGUGCACCCCUAGGCCCCAGCAGGAUACAUAUCACUGUCACUAUAGUCGUGAAACGUAGUGACUCGUGUUCCGACCAACUACCAGGCCUCACAAGCUCGGCGUCCUUUUUCAGCCCGAAUAGGUAUGGGACUCUUUUCUCUUCAUCGAGGGAUUUCAGGGAACCCGAAUUCCAAUCAGUCGUGAAUCGCCGUUCUGGGAGAGCGGUUAGAGGGACAUGCUGGGUGCCACUUACCGAUCGAAGGGAUUACAACAAUGAGGACAUUCAGAAUGCAGAUUUCACUGCGGCAGUAUGGGCAUCUCUGUUCGCUGAUCGGGCGGAUCGGUAUUCAGUCGCUCGUUGUUCCCACUUCUAUGUAUCUUGCCAUGAGCACUACUCUCAUCUGGCAAUCGCGUCCUGUUGGCUUCUAGAAUUUGGCAUUGCCCAGGUAAAAGAAUUAGUUAUGGCAAAUUUCCCAAAUACUAGGUUGUGGGACCGGCCUUCCUUGGUCUGUACAACGGAGCAGUGCCACCCCAAAUCCGAGAACCACAGCCAGGUUCCUACCCUAAUUGGACAGUGUAGGCGGUCGUCUAGAAGGAAACCUGUGAAGCGGUUAACGCCUCGUCGCAUGGUCCAGUCUCAGCUUGUAUCGAAUCAUAAAGUCGGUGUAGGGUGUCAAAGUUUGGUAGUCUCGUUCCCACCAGUGUGCACUCCACGCACACGUACGUACGGAUAUUCCCUAUUGUACAAAUGUACCCUCAAAAACCCCCACUCAAAUUCCUCUGCCGUGUUCCUUAUUGUCCACUUCAGCCUGUCGUAUCCUAAAACUGGUAUCUCGAUGAUCGAUUGCCCACAACAAAACCACUUUAUUAUUAUUCUCGAACUAGAGCUCGGGGCAUACUUCUGGUUUAUACCGAUAGUACGUCGGUCGAGGUGCAAAUGGCAAGAUCUAUACUCUCUUCGCUCAAGUGGGGGCGUUGUAGGCCGCAAUCCAUGGGCAGACUGGAUAUCACGUUAUCUAGAUAGGACCACGUUUCAAAUAGCUAGCCUUUACGCGUGGCCCCUUCCGUAUUCUGUUACUACGCACAAUAGUCGUCUGCAUCAGAUACCCUUACGCAUGACACGACCCCCAACCCGGGACGGAAAGACAUGUUCCAAUGUCAAGAGGGGACCCACCGAUCAGGGCAGGCGGAGUGGAACACAGCCCCUUUCAAGAGAAUACAGUAGACUACUUAGGUGUAUUAGCAAACCGGUUAAUGAUCAUUCUGUUAAGAGUGGGUUCACAUACUCCAGGGAGCAGCUGGUCUUGAGUCCAGAGGUAGGGCCCGCGGUGAUCGCACCGGAUCCACACAAAAACACAGCUAAUCUCAGGAGGUUUACCUAUUUGCCACUGUGUCCUUCUUACCGCAGGGACUCGUCCCCCGAUAUGUUCAGUUCAACGACUGCUCGUAGGCCCAGUAAUCACAGGCUAAAGGACGAACCCUGCCAAAGUUACGUUCGGUGCCAAUACCCCAUGGCCGAGUAUAUCUUAACGGUUAGAAUGCACGGAGUGGUCUUCGGCCCGGGCCUUCGACUCACAGAUCUUGGAUACAGAGCACGUCUCUUUCCGCGACGGUACUACCCCGCGAUGUGUUGCUGCCAGAACUUCCUAUACCUCUCCUUUCGCACUGAUCACAUUCUCUUAUUACCCGAUACACCUUUAGAACGACGUUUGUCGUGCCUUCUCCCUCAACUUGUAUUAAAUAAAUGGGAUUCCAGUCGUCUGGCGCACAGCGUUGUUCAGAGUAAUCUUCACAAUAUCCCGGGGCCCGGCGCAUCGCGUCAGACAGUCAAGCGGGAUCGUCAUCUUUUAAAUGGACUCACAGUGGUAUGGUUGGAGGUAAAGGCACGUACGGCGCAAGGUCCGGGCCUCCGCAGUGUUUUUAUGCAACCCCCCAGGGCUCCGAUGACGGAUUUAGGCUGUUAUUGGAAUCUUGCGUGUAACAGUGGGCUCGCACUGGAUGAAUCGACCUUGUACGAUGAUAUCCCGUGGUUGACCCAAUUUCAUCUCUUCUACGCAUAG'

test = [codon_table.get(test[i:i+3]) for i in range(0, len(test), 3)]

print(''.join(test[:-1]))

