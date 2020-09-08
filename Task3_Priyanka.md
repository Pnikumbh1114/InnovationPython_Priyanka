'''
1./ 11. 	Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
'''

elements = ["Priyanka", 2+3j, 45, 10.08, 6j-5, "Welcome", 45.98, 43, "Python", 10] 
print(elements)


'''
2./ 12. 	Create a list of size 5 and execute the slicing structure 
'''

random = [3, 5, 2, 6, 1]
print(len(random))
print(random[1:5])
print(random[-1:])
print(random[2:])
print(random[:])
print(random[2:5:2])


'''
3. Write a program to get the sum and multiply of all the items in a given list.
'''

list = [20, 10, 50, 30, 40]
add = sum(list)
print(add)

#Using for loop

product = 1
for element in list:
    product = product * element
print(product)

#Using while loop

i = 0
mult = 1
while True:
    if i < len(list):
        mult = mult * list[i]
        i = i + 1
    else:
        break

print(mult)


'''
4.   	Find the largest and smallest number from a given list.
'''

list = [45, 87, 23, 90]

print(max(list))
print(min(list))


'''
5. 	Create a new list that contains the specified numbers after removing the even numbers from a predefined list.
'''

predefined_list = [32, 45, 63, 78, 12]

for i in predefined_list:
    if i%2 == 0:
        predefined_list.remove(i)
    

print(predefined_list)


'''
6.	Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
'''

list = []

for num in range(1,6):
    square1 = num * num
    list.append(square1)


for num in range(26,31):
    square2 = num * num
    list.append(square2)

print(list)


'''
7.	Write a program to replace the last element in a list with another list.
#Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
#Expected output: [1,3,5,7,9,2,4,6,8]
'''

sample_data = [[1,3,5,7,9,10],[2,4,6,8]]
first_half = sample_data[0]
second_half = sample_data[1]
first_half.pop(len(first_half) - 1)

final_list = first_half + second_half

print(final_list)


'''
8.	Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
Expected Result: {1:10,2:20,3:30,4:40}
'''

a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)


'''
9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
Sample data (n=5)
Expected Output: {1:1,2:4,3:9,4:16,5:25}
'''

x = dict()
n = int(input("Enter number n :"))
for i in (1, n+1):
     x[i]=x*x
print(x)


'''
10. 	Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
34,67,55,33,12,98
The output should be:
[‘34’,’67’,’55’,’33’,’12’,’98’]
(‘34’,’67’,’55’,’33’,’12’,’98’)
'''

num = eval(input("Enter a sequence of comma separated numbers: "))

a = []
a = list(num)
print(a)

b=()
b = tuple(num)
print(b)



'''
13. 	Create a list of given structure and run 
	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
'''

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

#Access list [1, 2, 3, 4]
print("\nFirst output: ", x[5][:4])

#Access list [600, 700]
print("\nSecond output: ", x[6:8])

#Access list [100, 300, 500, 600, 800]
print("\nThird output: ", x[::2])

#Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
new_list = []
new_list = [x[::-1]]
print("\nFourth output: ", new_list)

#Access list [10]
print("\nFifth output: ", [x[5][5][0]])

#Access list [ ]
print("\nSixth output: ", x)


'''
14. 	Create a list of thousand numbers using range and xrange and see the difference between each other.
'''

x = list(range(1, 1001))
print("The range function output is", x)
y = xrange(1, 1001)
z = list(y)
print("The range function output is", z) 


'''
15. 	How Tuple is beneficial as compared to the list?

List is mutable whereas a tuple is immutable. 
Fields can't be changed in Immutable data structres while fields can be changed in mutable data structures.
So a tuple is used in a condition where the data stored should not be changed.
'''


'''
16. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
'''

new_list = []
for i in range (1,101):
    if i%3 == 0 and i%2 == 0:
        new_list.append(i)

print(new_list)


'''
17. 	Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.
'''

letter = "Innovation using Python"
new = letter[::-1]
print(letter)
print("\n")
print(new)
print("\n")
new2 = []

for i in range(len(new)):
    if new[i] == 'a' or new[i] == 'e' or new[i] == 'i' or new[i] == 'o' or new[i] == 'u' or new[i] == 'A' or new[i] == 'E' or new[i] == 'I' or  new[i] == 'O' or new[i] == 'U':
        new2[i] = new[i]

print(new2)


'''
18. 	Write a program in Python to iterate through the string “hello my name is Abcde” and print the string which has even length of the word.
'''

string = "hello my name is Abcde"
a = print(string.split())
string1 = []
for i in a:
    if len(i) % 2 == 0:
        string1.append(i)
        
print(string1)


'''
19. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
'''

x=[1,2,3,4,5,6,7,8,9,-1]
n = len(x)
pairs = []
for i in range(0, n):
    for j in range(i+1, n):
        if x[i] + x[j] == 8:
            pairs = pairs.append(x[i], x[j])

print(pairs)


'''
20. 	Write a program in Python to complete the following task:
Create two different lists as in even_list and odd_list
Ask the user to enter the number in the range of 1,50 and make sure if the entered number is even appended it to the even_list and if the entered number is odd append it to the odd list.
Keep that in mind you can only add 5 items in each list
Make sure once you entered the total 5 elements calculate the sum of the list and return the maximum out of the list.
'''

even_list = list()
odd_list = list()

while True:
    print("\n")
    num = int(input("Enter any number in the range 1-50: "))
    
    if len(even_list) > 5 and len(odd_list) > 5:
        print("\nBoth even and odd lists have 5 values")
        print("\nThe sum of even list is ", sum(even_list))
        print("\nThe maximum number from even list is ", max(even_list))
        print("\nThe sum of odd list is ", sum(odd_list))
        print("\nThe maximum number from odd list is ", max(odd_list))
        break
    
    elif num % 2 == 0:
        if len(even_list) > 4:
            print("\nMaximum of 5 elements can be appended in the even list")            
            continue
        else:
            even_list.append(num)
            print("\nNumber added to the even list")
    
    else:
        if len(odd_list) > 4:
            print("\nMaximum of 5 elements can be appended in the odd list")            
            continue
        else:
            odd_list.append(num)
            print("\nNumber added to the odd list")

print("\nThe even list is ", even_list)
print("\n")
print("\nThe odd list is ", odd_list)


'''
21. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement. 
 Example: 12abcbacbaba344ab  
                      Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
'''

string = "12abcbacbaba344ab"

demo = dict()
for i in string:
    if i in demo:
        demo[i] += 1
    elif i.isdigit():
        continue
    else:
        demo[i] = 1

print(demo)


'''
22.          Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''

tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1 = list()
for i in tuple1:
    if i%2 == 0:
        list1.append(i)

tuple2 = tuple(list1)
print(tuple2)


