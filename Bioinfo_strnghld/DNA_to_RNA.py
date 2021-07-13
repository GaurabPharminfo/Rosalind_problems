
DNA_str = input('Enter the DNA : ')

trans_char = DNA_str.maketrans("T","U")
RNA_str = DNA_str.translate(trans_char)

print(RNA_str)