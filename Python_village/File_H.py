
infl_name = input('Enter the filename : ')

with open (infl_name, 'r') as in_fl:
    lines = in_fl.readlines()

fl_name_ch = lambda str : str.replace('ini','out')
even_index = lambda x : x if (x+1) % 2 == 0 else None

new_lines = []
for i in range(0, len(lines)):
    i = even_index(i)
    if i != None:
        print(lines[i])
        new_lines.append(lines[i])
    

outfl_name = fl_name_ch(infl_name)

with open(outfl_name, 'w') as out_fl:
    out_fl.writelines(new_lines)