#identity:
'''
a = ["today", "tommorow", True, 0.5, False]
b = ["today", "tommorow", True, 0.5]

# print(a is not b)
#python variables are actually references to location in memory, 
# a and b are pointing to seperate places in memory locations(object references) until you make them point to each other
a=b
print(a is b)
print(a is not b)
'''

'''
#comparison operators(=,<,>,>=,<=,!=,!<)
a = 2
b = 6
print(a < b)
print(a > b)
#in python we can chain comparison operators
a=9
print(0 <= a <= 10)
'''

#"three" < 3 #python is strongly dynamically typed, we dont need to supply the variable or the object type

#membership
'''
p = (4, "monday", 10, -33, True)
print(2 in p)
print(2 not in p)

q = "today is tuesday"
print("today" in q)
'''

'''
a = "monday"
b = "tuesday"

print(a and b)
print(a or b)

'''
# Control Flow Statements
#if else statement
'''
if condition1:
	pass
elif condition2:
	pass
...
else:
	pass
'''
'''
a = 10
b = 3
c = 7
if (a>b and b<c):
	print("very so")
elif (a<b or c>b):
	print("not really true")
else:
	"adunno"
'''

#while loop: to test if a condition returns true, more than once:
'''
lessThan5 = 0
while lessThan5 < 5:
	print("Still < 5")
	lessThan5 += 1
	if lessThan5==3:
		break
	print("Thank you")
print("finished")
'''

'''
lessThan5 = 0
while lessThan5 < 5:
	print("Still < 5")
	lessThan5+=1
	if lessThan5==3:
		continue
	print("i'm waiting")
'''
'''
Countries = ["Nigeria", "Ghana", True, 1000, "America"]
for Country in Countries:
	print(Country)



Alphabets = "abcdefghijklmnopqrstuvwxyz"
for i in Alphabets:
	if i in "aeiou":
		print(i, "is a vowel") 
	else:
		print(i, "is a consonant")
	
'''
'''
try:
	x = int(input("please enter a number "))
	ansa = x/2
	print(ansa)
except ValueError as err:
	print(err)
'''
'''
name = "john "
name += "mike"
print(name)
'''

'''
list1 = ["Mango", "Orange", "Cashew", "Onion"]
list2 = ["Tomato", "20"]
print(type(list2))
#list1 += 5
#print(list1) #will return an object because an int is not iterable
print(list1 + list2)
list2 += ["cherry", "banana"]
print(list2)
'''

#returns the sum of all valid inputs,
#drops every invalid input politely
'''
total = 0
count = 0
while True:
	try:
		line = input("enter a number")
		if line:
			try:
				number = float(line) 
			except ValueError as ve:
				print(ve)
				continue
			total += number
			count += 1
			print(total)
	except EOFError:
		break
'''

#using functions
#methods are functions that are declared inside a class
'''
def add():
	a = float(input("enter your first no."))
	b = float(input("enter your second no."))
	print(a + b)
add()
'''
'''
def get_int():
		try:
			i = int(input("Enter a number or something convertible"))
			print("your age is", i)
		except ValueError as ve:
			print(ve)
get_int()

from datastructures import morse
print(len(morse))
'''

Malone = ['Sugar Wraith', 'Rich and Sad', 'Zack and Codeine', 'Psycho', 'Paranoid']
Ego_Menar = ['DYBMH', 'Fragile', 'Desperate', 'Wait', 'Change the World']
mal = Malone[3], Malone[0]
print(mal)
ego = Ego_Menar[1], Ego_Menar[4]
print(ego)
meg = mal + ego
print(meg)

for songs in meg:
	if len(meg)<=3:
		print(songs)
	else:
		print('none')
 

















