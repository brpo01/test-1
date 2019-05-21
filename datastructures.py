'''
#you can store more than one datatype in a list
list1 = ['Mathematics', 'Language', 'Science', 2000, False, 'Health Education']
#access the nth item
print(list1[2]);

#updating the list
list1[4] = True
print(list1)

#deleting items from a list
del list1[2]
print(list1)

#multiplication and concatenation
list2 = list1 + ['Agriculture', '10.7']
print(list2)

print(['Agriculture', '10.7'] * 3)

#length of list1
print(len(list1))
#membership 
print('Agric' in list2)

#iteration
print('START ITERATION')
for x in list1:
	print(x)
'''
'''
list1 = ['Mathematics', 'Language', 2000, False, 'Health Education']
'''
'''
for x in list1:
	if(list1.index(x) <= 2):
		print(x)

#indexing 
for x in list1:
	print(x, end= ' ')
'''
'''

for x in list1:
	if(list1.index(x) <= 4):
		print(x, end=' and ')
	else:
		print(x)

#Indexing
print(list1[-2])
print(list1[:2])
print(list1[2:])
print(list1[1:4])

#max
list2 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(max(list2))
print(min(list2))

#convert a tuple to list
tuple1 = (234, 'C++', False, 'Python')
list3 = list(tuple1)
print(list3)

#append
list3 = [234, 'C++' ,False, 'Python']
list4 = list3.append('c#')
list5 = list3 + ['C#']
print("for concatenation:",list5)
print("for append:",list4)

#count
list6 = [234, 'C++', False, 'Python', 'C++', 'C#']
print(list6.count("C++"))

print([234, 'C++', False, 'Python', 'c#', 'C#'].count("Python"))
print([234, 'C++', False, 'Python', 'c#', 'C#'].count("Jython"))
'''
#EXTENDING A RANGE INTO A LIST
'''
print(range(5))
for i in range(5):
	print(i, end= ' ')
'''

'''
list7 = list(("a", "b", "c", "d"))
print(list7)
new = list7.extend(range (5))
print(list7)
print(new)

#index
names = ['bolaji', 'aisha', 'daniel', 'david','aisha', 'taofeek']
print('first occurence of aisha', names.index('aisha'))

'''
'''
#POP(): returns and removes the last item
subjects = ['maths', 'english', 'science', 'language', 'culture', 'religion']
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())

'''
'''
#remove() :returns the last item and returns none
subjects = ['maths', 'english', 'science', 'language', 'culture', 'religion']
holder1 = subjects.pop()
holder2 = subjects.remove('english')

print(holder1)
print(holder2
'''

#reverse: reverses the list and returns none
'''
subjects = ['maths', 'english', 'science', 'language', 'culture', 'religion']
holder3 = subjects.reverse()
print(holder3)
print(subjects)

#sort():
subjects = ['maths', 'English', 'science', 'Language', 'culture', 'religion']
numbers = ["12","11","23","7"]
print(subjects.sort())
print(subjects)
numbers.sort()
print(numbers)
'''

'''
#Dictionaries: the compiler implements dictionaries and lists  as hash tables, dictionaries have keys(strings) and values(integers)
states_pop = {"Lagos":3567234, "Kano":4645376, "Abuja":1672357, "Ph":3123907, "Kd":2784123}
print(states_pop['Kano'])
#key error
#print(states_pop[1])

states_pop['Ogun'] = 3123578
print(states_pop)

states_pop['Kano'] = 123785
print(states_pop)

#defining an empty dictionary
names = {}
names['first'] = 'sen aba'
print(names)


#the KEYS AND THE values can BOTH recur
names = {'FIRST':'SEN BALA', 'SECOND':'JOHN UDEH', 'THIRD':'MARK THAND', 'FOURTH':'SEN BALA'}
print(names['FIRST'])

en_yor = {'One':'Ookan', 'Two':'eeji', 'Three':'eta', 'four':'eerin', 'five':'aarun'}
print(en_yor['Two'])
yor_ig = {'Ookan':'Otu', 'eeji':'abo', 'eta':'ato', 'eerin':'ano','aarun':'ise'}
print((yor_ig['eta']))

print(yor_ig[en_yor['One']])

#Rules
#YOU CANNOT USE MUTABLE TYPES AS KEY
#dic = {[1,2,3]:'abc'}
dico = {'abc':[1,2,3]}


#operations of dictionaries
#len(), del(k), k in d, k not in d
print('abc' in dico)
del dico['abc']
print(len(dico))
print(dico)

morse = {
	'A':'QW',
	'B':'QWER',
	'C':'QWERTY',
	'D':'QWERTYUI',
	'E':'QWERTYUIOP',
	'1':'AS',
	'2':'ASDF',
	'3':'ASDFGHJ',
	'4':'ASDFGHJKL',
	'5':'ASDFGHJKLXZ'
}

from datastructures import morse
print(len(morse))
'''

#pop()
en_yor = {'One':'Ookan', 'Two':'eeji', 'Three':'eta', 'Four':'eerin', 'five':'aarun'}
yor_ig = {'Ookan':'Otu', 'eeji':'abo', 'eta':'ato', 'eerin':'ano','aarun':'ise'}
#print(en_yor.pop('One'))
# print(en_yor.pop('Three'))


# eng = (input("ask for an english word ").lower())
# print(yor_ig[en_yor[eng]])

#if a pair cannot be popped, a key error will be raised
#print(en_yor.pop('six'))


#popitem()
capitals1 = {"Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Lome", "South Africa":"Johannesburg", "Mali":"Bamako"}
'''
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
#print(capitals.popitem())
print(capitals)

#we can prevent the errors from passing non-existent kesys using the member

if "Rivers" in capitals:
	print(capitals["Rivers"])

#we can also use #alternative, #get
print(capitals.get("Rivers", "Port Harcourt"))
'''
#copy():

capitals2 = {"United Kingdom":"London", "Russia":"Moscow", "Sweden":"Stockholm"}
capitals1.update()
updated_dic = capitals1.update(capitals2)
print(updated_dic)
print(capitals1)

#iteraing over a a dictionary
#print all items in the updated capitals1 dictionary

for a,b in capitals1.items():
	#print(a+":"+b)
	print(f'{a}:{b}')

#conversion between lists and dictionaries:
capitals1 = {"Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Lome", "South Africa":"Johannesburg", "Mali":"Bamako"} , {"France":"Paris"}
list1 = [capitals1]
print(list1[0])

morse = {
	'A':'QW',
	'B':'QWER',
	'C':'QWERTY',
	'D':'QWERTYUI',
	'E':'QWERTYUIOP',
	'1':'AS',
	'2':'ASDF',
	'3':'ASDFGHJ',
	'4':'ASDFGHJKL',
	'5':'ASDFGHJKLXZ'
}

'''
from datastructures import morse
print(morse['D'])
'''










