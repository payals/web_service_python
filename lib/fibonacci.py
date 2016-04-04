#!/usr/bin/python

def valid_input(i):
	try:
		float(i) # for int, long and float
	except ValueError:
		try:
			complex(i) # for complex
		except ValueError:
			return False
	if i == int(i):
		return True
	return False



def iterator():
	a, b = 0, 1
	while 1:
		yield a
		a, b = b, a + b



def fibonacci(fib_length):
	if not valid_input(fib_length):
		raise ValueError("invalid input - not integer")

	if fib_length < 1:
		raise ValueError("invalid input - less than one") 	

	if fib_length > 1000:
		raise ValueError("you can input a maximum of 1000")

	series = []
	a = iterator()
	for i in range(fib_length):
		series.append(a.next())
	return series
