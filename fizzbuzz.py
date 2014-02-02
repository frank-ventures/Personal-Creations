print ('Welcome to the Fizzbuzz Detector!')
usernum = int(input('Please enter a number to count up to: '))

for i in range(1, usernum+1):
	if (i % 3 == 0 and i % 5 == 0):
		print ('FIZZBUZZ')
	elif (i % 3 == 0):
		print ('Fizz')
	elif (i % 5 == 0):
		print ('Buzz')
	else:
		print(i)
