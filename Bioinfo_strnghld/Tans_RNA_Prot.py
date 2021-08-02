# Prompting input file name
fl_name = input('Enter the file name : ')

# Processing output file name
fl_name_ch = lambda str : str.split('.')[0]+'_out.'+str.split('.')[1]
outfl_name = fl_name_ch(fl_name)

# Reading input file content
with open(fl_name,'r') as in_fl:
    fl_data = in_fl.readlines()

RNA_str = fl_data[0].strip()

def codon2aa(codon):
    ''' Converting supplied codons to single letter amino acid code.'''
    codon_table = {
        'UUU' : 'F', 'CUU' : 'L', 'AUU' : 'I', 'GUU' :  'V',
        'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' :  'V',
        'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' :  'V',
        'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' :  'V',
        'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' :  'A',
        'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' :  'A',
        'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' :  'A',
        'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' :  'A',
        'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' :  'D',
        'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' :  'D',
        'UAG' : '', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' :  'E',
        'UAA' : '', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' :  'E',
        'UGU' : 'C', 'CGU' : 'R', 'AGU' : 'S', 'GGU' :  'G',
        'UGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' :  'G',
        'UGA' : '', 'CGA' : 'R', 'AGA' : 'R', 'GGA' :  'G',
        'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' :  'G'
    }
    print('{codon} = {aa}'.format(codon = codon, aa = codon_table[codon]))
    return codon_table[codon]

# Convert RNA sequence to codon list
str2codon = lambda str: [str[i:i+3] for i in range(0, len(str), 3)]
RNA_codon = str2codon(RNA_str)
print(RNA_codon)

# Translate RNA codon list to protein amino acid list
Trans_prot = list(map(codon2aa, RNA_codon))

# Convert amino acid list to protein sequence
Trans_prot = ''.join(map(str,Trans_prot))
print(Trans_prot)

#Writing output file
with open(outfl_name, 'w') as out_fl:
    out_fl.writelines(Trans_prot)

##