# a program that prints your name 100 times
name = ' Bola-Rotimi Praise'
your_name = (name * 100)

for item in your_name:
    print(f'my name is {name}')

# a program that prints integers 1-20
for x in range(21):
    square = x * x
    print(f'{x} --- {square}')


# triangle
triangle = [1, 2, 3, 4, 5, 6 ]
for num in triangle:
    print(num * '*')

# square
numbers = [14, 2, 2, 14]
for count in numbers:
    if count == 14:
        print(f'x' * count)
    else:
        print(f'x' + f'            ' + f'x')

# 'A' shape
for lines in range(4):
    if lines == 0:
        print('    *  ')
    elif lines == 1:
        print('  *   *')
    elif lines == 2:
        print(' *  *  *')
    else:
        print('*       *')

#factorial
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num = int(input("Enter a number: "))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print(f'The factorial of {num} is {factorial(num)}')

#recursive fxn
def calculate(number):
    if number == 1:
        return f'f(n) = 3'
    else:
        a = 3 ** num
        return (f"f(n) = {a}")
num = float(input('Enter a number: '))
print(calculate(num))



















