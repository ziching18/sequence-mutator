# sequence-mutator

<p>#bioinformatics</b>

The sequence mutator is a function that mutates a sequence according to a set of mutations provided by the user. Depending on the number of sequences, 2 functions are provided: ```mutate_seq``` and ```mutate_multiseq```. The FASTA sequence must be read/parsed using ```Bio.SeqIO``` and the mutated sequence will be returned as a ```SeqRecord```.
