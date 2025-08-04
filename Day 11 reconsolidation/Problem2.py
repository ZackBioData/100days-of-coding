from Bio import SeqIO

record = list(SeqIO.parse("rosalind_orf (2).fasta", "fasta"))
DNAseq = record[0].seq
forward_rna = DNAseq.transcribe() 
reverse_rna = DNAseq.reverse_complement().transcribe()

for frame in range(3):
        protein = forward_rna[frame:].translate(to_stop=False)
        aa_seq = str(protein)
        starts = [i for i in range(len(aa_seq)) if aa_seq[i] == 'M']
        for start in starts:
            sub = aa_seq[start:]
            stop = sub.find("*")
            if stop != -1:
                print(sub[:stop])
                
        protein = reverse_rna[frame:].translate(to_stop=False)
        aa_seq = str(protein)
        starts = [i for i in range(len(aa_seq)) if aa_seq[i] == 'M']
        for start in starts:
            sub = aa_seq[start:]
            stop = sub.find("*")
            if stop != -1:
                print(sub[:stop])