'''
1. Write a program to reverse a string.
Sample data: “1234abcd”
Expected Output: “dcba4321”
'''

def reverse(s):

    return s[::-1]

demo_str = "1234abcd"
result = reverse(demo_str)
print(result)


'''
2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def case_calculator(x):
    count_upper = 0
    count_lower = 0
    for i in range(len(x)):
        if x[i].isupper():
            count_upper += 1
        else:
            count_lower += 1
    print("No. of Upper case characters : ", count_upper)
    print("No. of Lower case Characters : ", count_lower)

user_input = str(input("Enter a string of upper and lower case characters: "))
case_calculator(user_input)


'''
3.        Create a function that takes a list and returns a new list with unique elements of the first list.
'''

def unique_function(old):
    new_list = []
    for i in old:
        if i not in new_list:
            new_list.append(i)
    return new_list


old_list = ["consultadd", 1, 3, 1, 5, 7, 3, "consultadd"]
result = unique_function(old_list)
print(result)


'''
4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
'''

inp = str(input("Enter hypen separated sequence of words as input: "))
user_input = list(inp().split("-"))

def sorting(user_input):
    user_input.sort()
    return "-".join(user_input)

result = sorting(user_input)
print(result)


'''
5.         Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Sample input:
Hello world
Practice makes perfect
Expected Output:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

stored = []
new_string = ""

def capitalize(stored, new_string):
    while True:
        user_input = str(input())
        if user_input == '':
            break
        else:
            stored.append(user_input)
    
    for i in stored:
        new_string = str(i.upper())
        print(new_string)
    

capitalize(stored, new_string)


'''
6.          Define a function that can receive two integral numbers in string form and compute their sum and print it in console.
'''

def sum():
    n1 = str(input("Enter the first number: "))
    n2 = str(input("Enter the second number: "))
    result = int(n1) + int(n2)
    return result


res = sum()
print("Sum is: ", res)


'''
7. Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
'''

def max():
    string1 = str(input("Enter String1: "))
    string2 = str(input(("Enter String2: "))
    if len(string1) > len(string2):
        print("The string with maximum length is: ", string1)
    elif len(string1) == len(string2):
        print("Both strings have equal length: \n", string1, "\n", string2)
    else:
        print("The string with maximum length is: ", string2)


max()


'''
8.        Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
'''

def square():
    demo = []
    for i in range(2,20):
        square = i*i
        demo.append(square)
        demo_tuple = tuple(demo)
    return demo_tuple


result = square()
print("The tuple is: ", result)


'''
9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
Example: If the limit is 3 , it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD
'''

limit = int(input("Enter the limit: "))

def showNumbers(limit):
    for i in range(0, limit+1):
        if i%2 == 0:
            print(i, "EVEN \n")
        else:
            print(i, "ODD \n")


showNumbers(limit)


'''
10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
'''

demo = []

def filter():
    for i in range (1, 21):
        if i%2 == 0:
            demo.append(i)
            return list(demo)

res = filter()
print(res)


'''
11. 	Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
Hints: Use map() to generate a list.
     	     Use filter() to filter elements of a list
            Use lambda to define anonymous functions
'''

demo = list(map(int, range(1,11)))

def even_number(n):
        if n%2 == 0:
            return n
    
filter_list = list(filter(lambda x:(x%2==0), demo))

print("The list of even numbers : ",filter_list)
#squared = lambda x: x*x
print("The squared list: ", list(map(lambda n:n*n, filter_list)))


'''
12. 	Write a function to compute 5/0 and use try/except to catch the exceptions
'''

try:
    def compute():
        res = 5/0
        return res

    result = compute()
    print(result)

except ZeroDivisionError:
    print("The number in the denominator is zero, which is why it cannot be calculated....Sorry!")


'''
13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
Goal : Turn [1,2,3,4,5,6,7] to 1234567 
'''

from functools import reduce

demo = [[1,2,3],[4,5],[6,7,8]]

result = (reduce((lambda x,y: x + y), demo))
print(result)


'''
14. (i) 
'''

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

'''
This program prints 2 which is in the finally block
'''

'''
(ii) 
'''

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()

'''
Try will give an error as there is a function called 'f(x,4)' where no such function name is defined.
Finally block prints 'after f'. In the end, it'll print 'after f?'.

Error
'after f'
'after f?'
'''
