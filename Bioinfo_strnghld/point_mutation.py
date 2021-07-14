# Prompting input file name
fl_name = input('Enter the file name : ')

# Processing output file name
# fl_name_ch = lambda str : str.split('.')[0]+'_out.'+str.split('.')[1]
# outfl_name = fl_name_ch(fl_name)

# Reading input file content
with open(fl_name,'r') as in_fl:
    fl_data = in_fl.readlines()

# parsing sequences from file data
seq1, seq2 = fl_data[0].strip(), fl_data[1].strip()

# calculating hamming distance between sequence
hD = 0
for i in range(0, len(seq1)):
    if seq1[i] != seq2[i]:
        hD += 1

print('Hamming Distance : ', hD)