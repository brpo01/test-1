#functions are first class objects
#classes are blueprints or prodcing objescts, there are some pre-defined classes

#simply prints the argument passed to it
def printer(arg):
	print(arg)
printer("Hello Class")

#converts celsius to farenheit

def farenheit(T_in_celsius):
	return(T_in_celsius * (9/5) + 32)
print(farenheit(20), "farenheit")

'''
tuple0 = []
tuple1 = [20, 5, 10.6, 7, 9]
for x in tuple1:
	tuple0.append(farenheit(x))
print(tuple0)
'''
'''
list0 = []
list1 = [7, 90, 3, 4]
for x in list1:
	list0.append(farenheit(x))
print(list0)
'''
'''
def sum_int(x,y):
	output = x+y
	return output
print(sum_int(5,6))
'''
'''
first = int(input('enter your number '))
second = int(input('enter your number '))
third = int(input('enter your number '))
fourth = int(input('enter your number '))
fifth = int(input('enter your number '))

def avg(): 
	output = (first+second+third+fourth+fifth)/5
	return output
print(avg())
'''
'''
def avg():
	empty = []
	first = int(input('enter your number '))
	empty.append((first))

	second = int(input('enter your number '))
	empty.append((second))

	third = int(input('enter your number '))
	empty.append((third))

	fourth = int(input('enter your number '))
	empty.append((fourth))

	fifth = int(input('enter your number '))
	empty.append((fifth))

	sum = first + second + third + fourth + fifth

	y = len(empty)
	print(empty)
	print(int(sum)/y)
avg()
'''
'''
def avg():
	list1 = []
	sum = 0
	x = 0
	while(len(list1) < 5):
		item = float(input('enter your number'))
		list1.append(item)
		x+=1
	for item in list1:
		sum+=item
	av = float(sum/len(list1))
	print(list1)
	print(av)
avg()
'''


def avg():
	empty = []
	sum = 0

	while (len(empty) < 5):
		item = float(input('enter you no'))
		empty.append(item)
	
	for item in empty:
		sum+=item
	z = len(empty)
	av = float((sum)/z)
	print(empty)
	print(av)
avg()















	







