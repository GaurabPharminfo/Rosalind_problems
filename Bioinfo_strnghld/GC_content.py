# Prompting input file name
fl_name = input('Enter the file name : ')

# Processing output file name
fl_name_ch = lambda str : str.split('.')[0]+'_out.'+str.split('.')[1]
outfl_name = fl_name_ch(fl_name)

# Reading input file content
with open(fl_name,'r') as in_fl:
    fl_data = in_fl.readlines()

# Parsing data from fasta file format
seq_data = dict()
identifier = None
for line in fl_data:
    if line.startswith('>'):
        identifier = line[1:].strip()
        seq_data[identifier] = ''
    else:
        seq_data[identifier] += line.strip()

print(seq_data)

# Calculating GC contetnt of parsed sequences
calc_GC = lambda seq : ((seq.count('G')+seq.count('C'))/len(seq))*100

GC_data = dict()
for seq_id in seq_data.keys():
    seq = seq_data[seq_id]
    GC_data[seq_id] = round(calc_GC(seq),6)

# Finding sequence with maximum GC content
max_from_dict = lambda x : max(x, key=x.get)
max_GC = max_from_dict(GC_data)
print(max_GC, GC_data[max_GC])

# Writing output file
with open(outfl_name, 'w') as out_fl:
    out_fl.writelines(max_GC+'\n'+str(GC_data[max_GC]))