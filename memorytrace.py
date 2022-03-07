#!/usr/bin/python3

def exercise1():
	a= 208
	b=210
	print("the id of a is ",id(a))
	print("the id of b is ",id(b))
	c=2000
	print("the id of c is ",id(c))
	add_two_thousands(c)

def add_two_thousands(Number):
		print("the id of Number is ",id(Number))


		
if __name__ == '__main__':
	exercise1()
