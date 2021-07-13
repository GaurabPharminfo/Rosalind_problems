
fl_name = input("Enter the file name : ")

with open(fl_name, 'r') as in_fl:
	lines = in_fl.readlines()

nums = lines[0].split(' ')
#print(nums, type(nums))

def fibonacci(n,m):
	f = [0, 1]
	for i in range(2, n+1):
		f.append(f[i-1] + f[i-2]*m)
	return f[n]


print(fibonacci(int(nums[0]),int(nums[1])))
