
dna_str = input('Enter the DNA string : ')
nt_arr = list(dna_str)

base_count = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

for nt in nt_arr:
    if nt in base_count:
        base_count[nt] += 1
    else:
        base_count[nt] = 1

print(' '.join(list(base_count.keys())))
print(' '.join([str(c) for c in base_count.values()]))