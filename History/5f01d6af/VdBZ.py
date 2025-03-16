a = int(input())

a = 0

while a == 0:
	try:
		if a == 0:
			print('a = 0')
			
		elif a <= 5:
			print('a < or = 5')
			
		elif 5 < a <= 10:
			print('a > 5 or = 10')
			
		elif a > 10:
			print('a > 10')
	
	except ValueError:
		print('you input invalid value, please try again')