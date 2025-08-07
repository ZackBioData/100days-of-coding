from Bio import SeqIO


records = list(SeqIO.parse("rosalind_hamm.fasta", "fasta"))

string_1 = str(records[0].seq)
string_2 = str(records[1].seq)

for bases in range(len(string_1)):
    if string_1[bases] != string_2[bases]:
        hamming_distance += 1   
print(hamming_distance)