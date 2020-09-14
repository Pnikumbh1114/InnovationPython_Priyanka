#1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except SyntaxError:
        print("Please enter a valid number: ")


#2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.

from sys import argv

while True:
    
    try: 
        file_name = input("Enter the file name: ")
        file_handler = open(file_name, 'r')
        reader = file_handler.read()
        print(reader)
        break
    except:
        print("The entered name is incorrect. Please enter the correct file name: ")
#       file_name = input("Please enter the correct file name: ")
    finally:
        file_handler.close()      
        

#3. 	Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits” 

while True:    
    number = input("Enter the numbers here: ")
    num = number.split()
    try:      
        if len(num) < 5:
            print(num)
            break
        else:
            raise Exception
    except:
        print("Please length is too short/long !!! Please provide only four digits\n")
    

#4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

user_email = input("Enter UserEmail: ")
pw_1 = input("Enter Password: ")
count = 0

while count < 3:  
    pw_2 = input("Re-Type Password: ")
    
    try:
        if pw_1 == pw_2:
            break 
        else:
            raise Exception

    except:
        print("Please retype the password. ")

        
#5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept.



'''
6. 	Read any file using Python File handling concept and return only the even length string from the doc.txt file.
Consider the content as: 
	Hello I am a file 
	Where you need to return the data string 
	Which is of even length 
	Make sure you return the content in 
	The same link as it is present.
'''
import os
os.getcwd()
os.chdir("C:/Users/Nishant Nikumbh/Desktop/PDCA")
from sys import argv

try:
    file_handler = open('doc.txt', 'r')
    reader = file_handler.read()
    print(reader)

    reader1 = reader.split()
    reader2 = []
    for i in reader1:
        if len(i)%2==0:
            reader2=reader2.append(i)
            print(reader2)
    print(" ".join(reader2))
#print(reader2)
except:
    print("Enter the right name")

finally:
    file_handler.close()
            

#7. Replace vowels with letter X

s = "consultadd"

for i in s:
    if i in 'aeiou':
        print(s.replace(i, "X"))
       