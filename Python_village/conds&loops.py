
odd = lambda x : x if x % 2 != 0 else 0

ints = input('Enter integers : ').split(' ')

odd_sum = 0
for x in range(int(ints[0]),int(ints[1])):
    odd_sum += odd(x)
    
print('Sum of the odd numbers between given numbers : ', odd_sum)