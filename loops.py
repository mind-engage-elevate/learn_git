limit = 20
print_string = 'FizzBuzz'
for i in range(1, (limit + 1)):
	if i % 15 == 0:
		print(print_string)
	elif i % 5 == 0:
		print(print_string[4:])
	elif i % 3 == 0:
		print(print_string[0:4])
	else:
		print(i)
print('one liner:')
print('\n'.join('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or str(i) for i in range(1, (limit + 1))))
