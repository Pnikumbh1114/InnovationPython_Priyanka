'''
1.	Create three variables in a single line and assign different values to them and make sure their data types are different. Like one is int, another one is float and the last one is a string.
'''

x, y, z = 2, 3.0, "Welcome!"

print(type(x))
print(type(y))
print(type(z))



'''
2. 	Create a variable of value type complex and swap it with another variable whose value is an integer.
'''

x = 2 + 3j
y = 10 
print(x)
print(y)
#y = complex(y)
#print(y)
x, y = y, x
#x = int(x)
print (x)
print(y)


'''
3. 	Swap two numbers using the third variable as the result name and do the same task without using any third variable.
'''

x = 10
y = 20
temp = x
x = y 
y = temp
print(x)
print(y)

a = 10
b = 20
a, b = b, a
print(a)
print(b)


'''
4. 	Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
'''

x = raw_input('Enter a value: ') for python2

x = input('Enter a value: ')  for python3


'''
5. 	Write a program to complete the task given below:
Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
Use z for adding 30 into it and print the final result by using variable results.
'''

x = eval(input('Enter a number between 1-10: '))
y = eval(input('Enter a number between 1-10: '))
z = x + y
res = z + 30
print(res)


'''
6. 	Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc
'''

input = eval(input('Enter something: '))
print("The input value data type is : ", type(input))


'''
7. 	Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:   https://capitalizemytitle.com/camel-case/)
'''
x = input("Enter a string in camelCase: ")
print(x)
y = input("Enter a string in LadderCase: ")
print(y)
z = input("Enter a string in UPPERCASE: ")
print(z)

'''
8. If one data type is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ variable again, will it change the value? If yes, why?

Ans: As Python is imperative, any variable which is assigned a value can be updated ahead in the program without any error.
'''
a = 10
print(type(a))

a = 'abc'
print(type(a))