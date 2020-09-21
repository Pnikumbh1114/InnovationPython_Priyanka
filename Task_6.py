#1. Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.

list1 = list(map(int, range(1,51)))
list2 = list(filter(lambda x: (x%7 == 0), list1))
list3 = list(filter(lambda x: (x%3 != 0), list2))
print(list3)


#2. 	Write a program in Python to  multiple the element of list by itself using a traditional function and pass the function to map to complete the operation.

def mult(n):
    return n*n

demo = [2, 5, 7, 3, 1, 9]
print(list(map(mult, demo)))


#3. Write a program to Python find out the character in a string which is uppercase using list comprehension.

demo = "HeLLo WorLD"
demo_res = [i for i in demo if i.isupper()]
print(demo_res)


#4. 	Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
#Student = ['Smit', 'Jaya', 'Rayyan']
#capital = ['CSE', 'Networking', 'Operating System']

student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

res = {k:v for (k,v) in zip(student, capital)}
print(res)


#6. 	Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

input_string = "Consultadd Training"

def rev(x):
    yield x[::-1]

res = rev(input_string)
print(res)
while True:
    try:
        a = next(res)
        print(a)
    except:
        break


#7. 	Write any example on decorators.

def make_pretty(function):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()


#8. 	Learn about What is FRONT END and its Technologies and Tools
#Make sure to mention at least 5 top notch technologies of Frontend.
#Also mentioned the name of companies using those 5 technologies individually
'''
1. ReactJS - Netflix uses React on Gibbon — their platform for low-performance TV devices and has been a favorite amongst the developer community. 
            Other alluring features of ReactJS like initial loading period, runtime performance, etc. are playing an important role in making Netflix as popular as it is today.
2. AngularJS - Weather.com is one of the top weather forecasting online report website. It’s also one the big websites using AngularJS.
3. NodeJS - World’s largest retail chain, Walmart, is ambitiously plunging into the online commerce space. 
            This endeavor of theirs to go online is being supported by Node.js which is their framework of choice. 
            Walmart chose to go with the trend and take the risk of involving a fairly newer technology than going with the tried and tested frameworks. 
            The organization offered its clients with newer, more sophisticated features by entirely re-engineering their mobile application. 
            Node.js’ asynchronous I/O mechanism along with its single threaded event loop models can help Walmart handle concurrent requests
4. React - React is the most powerful and highly used front-end technologies. It is an open-source front-end library released and licensed under MIT in 2013. 
            React is supported and maintained by the tech giant Facebook.
            To enable developers with code reusability and fast debugging, React splits the code into components. 
            The React-based appellations are SEO friendly and highly responsive.
5. Bootstrap - Bootstrap was released on 19th August 2011 under MIT license. 
                It is an open-source CSS framework to build dynamic websites and web applications. It is built by Mark Otto at Twitter as a framework for consistency.
'''