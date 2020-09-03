'''
1.	Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “c” as a string
If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.
'''

x = eval(input("Enter a number: "))

if x%3==0 and x%5==0:
    print("Consultadd Python Training")
elif x%3==0:
    print("Consultadd")
elif x%5==0:
    print("c")



'''
2. 	Write a program in Python to perform the following operator based task:
Ask the user to choose the following option first:
If User Enter 1 - Addition 
If User Enter 2 - Subtraction
If User Enter 3 - Division
If USer Enter 4 - Multiplication
If User Enter 5 - Average
Ask the user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
Ask the user to enter two more numbers as first1 and second2 for calculating the average as soon as the user chooses an option 5.
In the end, if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time users can perform one action at a time.
'''

option = int(input("Choose an option from the following: 1-Addition, 2-Subtraction, 3-Division, 4-Multiplication or 5-Average): ")) 

if option <= 5 and option >= 1:
    variable1 = int(input("Enter the first value: "))
    variable2 = int(input("Enter the second value: "))
    if option == 1:
        result = variable1 + variable2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    elif option == 2:
        if variable1 > variable2:
            print("NEGATIVE")
        else:
            result = variable1 - variable2
            print(result)
    elif option == 3:
        result = variable1 / variable2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    elif option == 4:
        result = variable1 * variable2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    elif option == 5:
        var3 = int(input("Enter third value: "))
        var4 = int(input("Enter fourth value: "))
        result = (var3 + var4 + variable1 + variable2) / 4
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
else:
    print("Invalid option!!")



'''
3. 	Write a program in Python to implement the given flowchart:
'''

a = 10
b = 20
c = 30

avg = (a + b + c) / 3
print("avg = ", avg)

if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, c")
elif avg > a and avg > b:
    print("avg is higher than a, b")
elif avg > a and avg > c:
    print("avg is higher than a, c")
elif avg > b and avg > c:
    print("avg is higher than b, c")
elif avg > a:
    print("avg is just higher than a")
elif avg > b:
    print("avg is just higher than b")
elif avg > c:
    print("avg is just higher than c")
    

'''
4.  Write a program in Python to break and continue if the following cases occur:
If a user enters a negative number just break the loop and print “It’s Over”
If a user enters a positive number just continue in the loop and print “Good Going”
'''

num = int(input("Enter a number: "))

while(num >= 0):
    print("Good Going")
    num = int(input("Enter a number again: "))
print("Its over")


'''
5.   Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
'''

for i in range (2000,3201):
    if i%7 == 0 and i%5 !== 0:
        print (i)


'''
6. What is the output of the following code examples?

x=123 
for i in x:
	print(i)

OUTPUT: ERROR 

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(“error”)

OUTPUT: 0 
        1  
        2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break

OUTPUT: 0
        1
        2
        3
        4
'''  



'''
7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
    
   Expected output: 0 1 2 4 5
Note: Use the ‘continue’ statement
'''

for num in range(0, 7):
    if num == 3 or num == 6:
        continue
    print(num)


'''
8.  Write a program that accepts a string as an input from the user and calculates the number of digits and letters.
     Expected output: consul12
     Letters 6
     Digits 2
'''

x = input('Enter a string: ')
letters = 0
digits = 0

for c in x:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
print("Letters: ", letters)
print("Digits: ", digits)


'''
9. Read the two parts of the question below: 
 Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question of whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
'''

#PART 1, Lucky number is 9

guess = int(input("Guess the lucky number: "))

while True:
    if guess == 9:
        print("Congratulations!")
        break
    else:
        print("Sorry! No Luck this time!")


#PART 2, Lucky number is 9

number = int(input("Guess the lucky number: "))

while True:
    if number == 9:
        print("Congratulations! \n")
        break
    else:
        print("Sorry, no luck this time \n")
        answer = input("Do you want to try again? (Yes/No): ")
        if answer == "No":
            break
        else:
            number = int(input("Guess the lucky number again: "))



'''
10.  Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
           		counter=1
		While counter <= 5:
			print(“Type in the”, counter, “number”
			counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess, it stops and prints “Game over!”.
'''


#Lucky number is 10

counter = 1

while counter <= 5:
    print("Attempt ", counter, ":")
    number = int(input("Guess the number: "))
    if number == 10:
        print("Good guess! \n")
        if counter == 5:
            break
    else:
        if counter == 5:
            break
        else:
            print("Try again! \n")
    counter += 1

print("Game over!")



'''
11.  In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.
'''


#Lucky number is 10

counter = 1

while counter <= 5:
    print("Attempt ", counter, ":")
    numb = int(input("Guess the number: "))
    if numb == 10:
        print("Good guess! \n")
        break
    else:
        if counter < 5:
            print("Try again! \n")
        else:
            print("Sorry but that was not very successful \n")
            break
    counter += 1

print("Game over!")
