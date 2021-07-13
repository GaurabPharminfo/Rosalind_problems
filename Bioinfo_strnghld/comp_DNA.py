
infl_name = input('Enter the file name : ')
with open(infl_name,'r') as in_fl:
    lines = in_fl.readlines()
    
DNA_str = ''
for line in lines:
    DNA_str += line
   
print(DNA_str)

reverse = lambda str : str[-1:-(len(str)+1):-1]
rev_DNA_str = reverse(DNA_str)

compliments = rev_DNA_str.maketrans("ACGT","TGCA")
revComp = rev_DNA_str.translate(compliments)

print(revComp)