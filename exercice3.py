#!/usr/bin/python3
# Program A
def evilGetLength1(ilist):
	length = len(ilist)
	del ilist[0:length] # Muhaha: clear the list
	return length # drawing A here
mylist = [12.8, -14.9, 16.6, -3.0]
l = evilGetLength1(mylist)
print(mylist) # predict the answer
print(l) # predict the answer


# Program B
def evilGetLength2(ilist):
	length = len(ilist)
	ilist = [] # Muhaha: clear the list
	return length # drawing B here
mylist = [12.8, -14.9, 16.6, -3.0]
l = evilGetLength2(mylist)
print(mylist) # predict the answer
print(l) # predict the answer