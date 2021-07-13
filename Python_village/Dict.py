
in_str = input('Enter the string : ')

word_list = in_str.split(' ')

count_dict = {}

for word in word_list:
    if word in count_dict.keys():
        count_dict[word] += 1
    else:
        count_dict[word] = 1

for word in count_dict.keys():
    print(word, count_dict[word])