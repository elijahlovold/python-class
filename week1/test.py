"""
variable types: 

* int 
* float

* str 

operators: 
= + - * / **
& | == != > < <= >=

<< >> ^ 
"""

# basic variable creation
x = 2
result = x**4   # computer x^n
print(result)

balance = 34
print(balance)

foo = 20
print(balance)

foo = 323
foo = int(323.234)

foo = True
foo = False

foo = "hello"
foo = 'hello'

string1 = "hello" 
string2 = " world"

output = "hello world"

num1 = 234
num2 = 98

output = ((num1 + num2) * num1 - num2) / num1

num1 = int(input("input num1"))
num2 = int(input("input num2"))

output = num1 + num2
output *= num1 
output -= num2 
output /= num1 

print(output)


# basic calculator example
num1 = int(input("nm1: "))
num2 = int(input("nm2: "))

operation = input("operation: ")

if (operation == "add") | (operation == "+"): 
    print(num1 + num2)

if operation == "sub": 
    print(num1 - num2)

if operation == "mult": 
    print(num1 * num2)

if operation == "div": 
    print(num1 / num2)


