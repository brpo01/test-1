#Strings in python
name = "Jon Bellion"
print(name[0])

#python strings are immutable
#name[3] = "c"

#we can convert python strings
# num1="55"
# print(type(num1))
# num2=int(num1)
# print(type(num2))

'''
num = "55"
int(num)
print(type(num))
'''

#object references
x='blue'
y='green'
z=x
print(x,y,z)

#we can rebind the variables
z=y
print(x,y,z)

x=z
print(x,y,z)

'''
route=1000
print(route, type(route))
route="north"
print(route, type(route))
'''

'''
python keywords
and exec not
assert finally or
continue global raise
def if return
del import try
elif in while
else is with pass

'''

'''
#collection datatypes
1.lists: -mutable
'''
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
days[0] = 'Aje'
print(days)

words=['book', False, 'Wednesday', 234]
words[2] = True
print(words)


#2. Tuples
'''
countries = ('Nigeria', 'UK', 'Ghana', 'Togo', 'Austria')
#they are unmutable
countries[2] = "Lagos"
print(countries)
'''
#python sequenes are sized - they are passed to the len() function

'''
print(len("bolaji"))
print(len(['monday', 'tuesday', False, 501]))
'''
true="God is good"
x=['zebra', 49, -987, "monkey", true]
x.append("more")
print(x)

