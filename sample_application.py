from Bio.Seq import *
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from sequence_mutator import *

# read FASTA sequence
prot = SeqIO.read("orf1ab/nsp3.fasta", "fasta")
mutations = {
    37: 'R',
    1264: '-',
    1265: 'I',
    1891: 'T'
}

seq1 = mutate_seq(prot, mutations)
print(seq1)

### ======================================================== ###

# read FASTA sequences
prefix = 
    ["nsp1",
    "nsp2",
    "nsp3",
    "nsp4",
    "nsp5",
    "nsp6",
    "nsp7",
    "nsp8",
    "nsp9",
    "nsp10",
    "nsp11",
    "nsp12",
    "nsp13",
    "nsp14",
    "nsp15",
    "nsp16"]
prots = []
for p in prefix:
    file = SeqIO.read("orf1ab/"+p+".fasta", "fasta")
    prots.append(file)
    
# define mutations in dict
o1_nsp1 = {}
o1_nsp2 = {}
o1_nsp3 = {
    37: 'R',
    1264: '-',
    1265: 'I',
    1891: 'T'
}
o1_nsp4 = {
    491: 'I'
}
o1_nsp5 = {
    131: 'H'
}
o1_nsp6 = {
    104: '-',
    105: '-',
    106: '-',
    188: 'V'
}
o1_nsp7 = {}
o1_nsp8 = {}
o1_nsp9 = {}
o1_nsp10 = {}
o1_nsp11 = {}
o1_nsp12 = {
    322: 'L'
}
o1_nsp13 = {}
o1_nsp14 = {
    41: 'V'
}
o1_nsp15 = {}
o1_nsp16 = {}
o1_mutations = [
    o1_nsp1,
    o1_nsp2,
    o1_nsp3,
    o1_nsp4,
    o1_nsp5,
    o1_nsp6,
    o1_nsp7,
    o1_nsp8,
    o1_nsp9,
    o1_nsp10,
    o1_nsp11,
    o1_nsp12,
    o1_nsp13,
    o1_nsp14,
    o1_nsp15,
    o1_nsp16
]

mutated = mutate_multiseq(prots, o1_mutations)
print(mutated)
