
str = input('Enter the string : ')
ints = input('Enter the integers : ').split(' ')

str_to_int = lambda a: [ int(x) for x in a]
ints = str_to_int(ints)

substr = lambda i, str: str[i[0]:i[1]+1]

print(substr(ints[0:3],str),substr(ints[2:],str), sep=' ')