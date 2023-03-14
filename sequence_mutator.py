### Code to mutate sequences, either for 1 sequence of list of sequences

"""
Mutate 1 sequence with 1 set of mutations
Input:
prot - SeqRecord fasta sequence
mutations - dict of all mutations, key = position, value = mutation
var - string for prefix of new name (optional)
write - whether to write mutated sequence to file (optional, False by default)
save_path - path to save file to (optional, current directory by default)
Returns:
mutated sequence
"""
def mutate_seq(prot, mutations, var="", write=False, savepath=""):
    new_seq = []
    for i,a in enumerate(prot.seq):
        chg = False
        for j in mutations.keys():
            if i == j:
                print("changed: {}{}{}".format(a,i,mutations[j]))
                new_seq.extend(mutations[j])
                chg = True
            #else:
        if chg == False:
            new_seq.extend(a)
    new_seq = ''.join(new_seq)
    new_name = var+"_"+prot.id
    seq_rec = SeqRecord(Seq(new_seq), 
                    id=new_name, 
                    name=new_name,
                    description=new_name)
    if write == True:
        SeqIO.write(seq_rec, save_path+new_name+".fasta", "fasta") # save in current directory unless specified
    
    return seq_rec
  
"""
Mutate list of sequences with list of sets of mutations
Input:
prots - list of SeqRecord fasta sequences [...]
mutations - list of dict of all mutations, key = position, value = mutation; [{},{}...,{}]
var - string for prefix of new name (optional)
write - whether to write mutated sequences to file (optional, False by default)
save_path - path to save file to (optional, current directory by default)
Returns:
list of mutated sequences
"""
def mutate_multiseq(prots, mutations, var="", write=False, save_path=""):
    new_seqs = []
    for d in range(len(prots)):
        print("seq{}".format(d+1))
        new_seq = []
        for i,a in enumerate(prots[d].seq):
            chg = False
            for j in mutations[d].keys():
                if i == j:
                    print("changed: {}{}{}".format(a,i,mutations[d][j]))
                    new_seq.extend(mutations[d][j])
                    chg = True
                #else:
            if chg == False:
                new_seq.extend(a)
        new_seq = ''.join(new_seq)
        new_name = var+"_"+prots[d].id
        seq_rec = SeqRecord(Seq(new_seq), 
                        id=new_name, 
                        name=new_name,
                        description=new_name)
        if write == True:
            SeqIO.write(seq_rec, save_path+new_name+".fasta", "fasta")
        new_seqs.append(seq_rec)  
        
        return new_seqs
