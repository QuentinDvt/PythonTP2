#!/usr/bin/python3

# Program A
a = [1, 2, 3]
b = a
b[0] = 2 # draw the state of memory now ==> drawing #A
print(a) # predict the answer [1, 2, 3]
print(b) # predict the answer [2, 2, 3]

# Program B
a = [1, 2, 3]
b = a + []
b[0] = 2 # draw the state of memory now ==> drawing #B
print(a) # predict the answer
print(b) # predict the answer

# Program C
a = [1, 2, 3]
b = []
for i in a :
	b.append(i)
b[0] = 2 # draw the state of memory now ==> drawing #B
print(a) # predict the answer
print(b) # predict the answer