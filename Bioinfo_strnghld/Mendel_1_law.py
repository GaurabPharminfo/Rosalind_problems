from itertools import combinations


# Prompting input file name
fl_name = input('Enter the file name : ')

# Reading input file content
with open(fl_name,'r') as in_fl:
    fl_data = in_fl.readlines()
k, m, n = map(int,fl_data[0].split())

# Different possiblities of mating for randomly selecting
# two mating organism (Given : Any two organisms can mate)
# along with probability of individual produced possessing
# a dominant allele.
# Probabilities are determined by Punnet square visualization.

probs = {
    ('AA', 'AA'): 1.00,
    ('AA', 'Aa'): 1.00,
    ('AA', 'aa'): 1.00,
    ('Aa', 'Aa'): 0.75,
    ('Aa', 'aa'): 0.50,
    ('aa', 'aa'): 0.00
}

# Enumerating total organisms in the population
pool = ['AA'] * k + ['Aa'] * m + ['aa'] * n

# Enumerating mating pairs
matings = list(combinations(pool, 2))

# Calculating total probability of dominant individual
sum = 0
for mating in matings:
    sum += probs[mating]

# Calculating probability of individual with dominant allele
# produced after a mating
res_prob = round((sum/len(matings)), 5)

print(res_prob)