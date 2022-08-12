def Patternn(pattern):
    for i in range(largest):
	    for j in range(len(numbers)):
		    print(pattern[j][i], end=' ')
	    print()
		
def Patterrn(arr):
	pattern = []
	for number in numbers:
		col = []
		for i in range(largest-1, -1, -1):
			if int(number) < largest:
				if i > int(number) - 1:
					col.append(' ')
				else:
					col.append('*')
			else:
				col.append('*')
		pattern.append(col)
	return(pattern)

numbers = input('Enter the Numbers:').split(' ')
largest = int(max(numbers))
Patternn(Patterrn(numbers))
