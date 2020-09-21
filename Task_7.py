'''
1.	Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
'''

from math import sqrt

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')                     
D = [str(round(calc(int(i)))) for i in D]  
print(",".join(D))


#2.         Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

sqr = Square(3)
print("Area = ", sqr.area())      

print(Square().area())  


'''
3. Create a class to find the three elements that sum to zero from a set of n real numbers.
Input array: [-25,-10,-7,-3,2,4,8,10]
Output: [[-10,2,8],[-7,-3,10]]
'''
class sum_zero:

    def findTriplets(self, arr, n): 
        found = True
        for i in range(0, n-2): 
        
            for j in range(i+1, n-1): 
            
                for k in range(j+1, n): 
                
                    if (arr[i] + arr[j] + arr[k] == 0): 
                        print(arr[i], arr[j], arr[k]) 
                        found = True
        
        if (found == False): 
            print(" not exist ") 
        
arr = [-25,-10,-7,-3,2,4,8,10] 
n = len(arr) 
sum_zero().findTriplets(arr, n)


'''
4.          What is the output of the following code? Explain your answer as well.

class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
Output:
0 1
Reason: when main() function is called, object b of Derived_Test class is created which also inherits the properties of Test class.
 

class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main())
Output:
Error
TypeError: super() takes at least 1 argument (0 given) 

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
 
    print(obj.x, obj.y)
main()
Output:
(3, 1)
When the statement as "A.__init__(self, 3)" is executed, it passes value of x as 3 and obj.count() function is called, it increments the value of y by 1.
 
 
class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
 
    def multiply(self, i):
        self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
 
    def multiply(self, i):
        self.i = 2 * i;
obj = B()

Output: Error
TypeError: super() takes at least 1 argument (0 given)
The value for i isn't provided.
'''

'''
5.	Create a Time class and initialize it with hours and minutes.
Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Make a method displayTime which should print the time.
Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
'''

class Time():

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins

  def addTime(t1, t2):
    sum = Time(0,0)
    if t1.mins+t2.mins > 60:
      sum.hours = (t1.mins+t2.mins)/60
    sum.hours = sum.hours+t1.hours+t2.hours
    sum.mins = (t1.mins+t2.mins)%60
    return sum

  def displayTime(self):
    print "Time is",self.hours,"hours and",self.mins,"minutes."

  def displayMinute(self):
    print (self.hours*60)+self.mins

x = Time(2,50)
y = Time(1,20)
z = Time.addTime(x,y)
print(z)
print(z.displayTime())
print(z.displayMinute())



''''
6.           Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
yearPasses() should increase the  instance variable by .
amIOld() should perform the following conditional actions:
If , print You are young..
If  and , print You are a teenager..
Otherwise, print You are old..	
Sample Input:
4
-1
10
16
18
Sample Output:
Age is not valid, setting age to 0.
You are young.
You are young.
 
You are young.
You are a teenager.
 
You are a teenager.
You are old.
 
You are old.
You are old.
'''

class Person:
    
    def __init__(self,initialAge):
        if initialAge <0:
            self.age= 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age=initialAge
            
    def amIOld(self):
        if self.age>32:
            print('You are old.')
        elif self.age<=32 and self.age>18:
            print('You are young.')
        else:
            print('You are teenager.')
            
    def yearPasses(self):
        self.age+=1
        
a = int(input())

for i in range(0, a):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    p.yearPasses()
