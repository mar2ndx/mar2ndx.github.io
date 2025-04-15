---
title: 【Tech】 Python learning notes
category: unknown
tags: technology
comments: true
date: 2015-05-31 00:00:00
---


# Python Basics

Python does not use brackets to structure code, instead it uses whitespaces.

## To define a variable 

you do not have to specify the datatype.

## find the datatype:

    print type(x)

## comment
    # This is a single line comment
    ''' This is a multi-line Python
    comment. '''

## ask the user for input 

using the raw_input function:

    #!/usr/bin/env python

    x = int(raw_input("Enter x:"))
    y = int(raw_input("Enter y:"))

    sum = x + y
    print sum

In the latest Python version you can use the input() function instead:

    x = int(input("Enter x:"))

## do operations on strings:

    s = "Hello Python"
    print s       # prints whole string
    print s[0]    # prints "H"
    print s[0:2]  # prints "He"
    print s[2:4]  # prints "ll"
    print s[6:]   # prints "Python"
    print s + ' ' + s # print concatenated string.
    print s.replace('Hello','Thanks') # print a string with a replaced word

### Python String compare

    sentence = "The cat is brown"
    q = "cat"

    if q == sentence:
        print 'equal'
    else:
        print 'not equal'

### Python String contains

    sentence = "The cat is brown"
    q = "cat"

    if q in sentence:
        print q + " found in " + sentence

## list

    l = [ "Drake", "Derp", "Derek", "Dominique" ]

    print l     # prints all elements
    print l[0]  # print first element
    print l[1]  # prints second element

    l.append("Victoria")   # add element.
    print l                # print all elements
    l.remove("Derp")       # remove element.
    l.remove("Drake")      # remove element.
    print l                # print all elements.

    l.sort()    # sorts the list in alphabetical order
    l.reverse() # reverse order.

iteration: 

    items = [ "Abby","Brenda","Cindy","Diddy" ]

    for item in items:
        print item

## A tuple is a sequence of data. 

It is defined as a sequence of elements separated by a comma.

    point = (3,4)
    point2 = (2,6,12)

    print point
    print point[0]
    print point[1]

    print point2
    print point2[0]
    print point2[1]

## A dictionary 

is an unordered set of key:

    words = {}
    words["Hello"] = "Bonjour"
    words["Yes"] = "Oui"
    words["No"] = "Non"
    words["Bye"] = "Au Revoir"

    print words            # print key-pairs.
    del words["Yes"]       # delete a key-pair.
    print words            # print key-pairs.
    words["Yes"] = "Oui!"  # add new key-pair.
    print words            # print key-pairs.

Output:

    {'Yes': 'Oui', 'Bye': 'Au Revoir', 'Hello': 'Bonjour', 'No': 'Non'}
    {'Bye': 'Au Revoir', 'Hello': 'Bonjour', 'No': 'Non'}
    {'Yes': 'Oui!', 'Bye': 'Au Revoir', 'Hello': 'Bonjour', 'No': 'Non'}

## Datatype casting

<table style="width:100%; " class="easy-table easy-table-cuscosky "><thead><tr><th>Function</th><th> Description</th></tr></thead><tbody><tr><td>int(x)</td><td> &nbsp;Converts x to an integer</td></tr><tr><td>long(x)</td><td> Converts x to a long integer</td></tr><tr><td>float(x)</td><td> Converts x to a floating point number</td></tr><tr><td>str(x)</td><td> Converts x to an string. &nbsp;x can be of the type float. integer or long.</td></tr><tr><td>hex(x)</td><td> Converts x integer to a hexadecimal string</td></tr><tr><td>chr(x)</td><td> Converts x integer to a character</td></tr><tr><td>ord(x)</td><td> Converts character x to an integer</td></tr></tbody></table>

    x = 3
    y = 2.15315315313532

    print "We have defined two numbers,"
    print "x = " + str(x)
    print "y = " + str(y)

    a = "135.31421"
    b = "133.1112223"

    c = float(a) + float(b)
    print c

## if

    print "Guess my age"
    guess = int(raw_input("Guess: "))

    if guess > 10 and guess < 20:
        print "In range"
    else:
        print "Out of range"

## function

    def doA():
        a = 5

    def doB(a):
        print a   # this will work

    doB(3)

## For loop 1

    items = [ "Abby","Brenda","Cindy","Diddy" ]

    for item in items:
        print item

## For loop 2

    for x in range(1,10):
        for y in range(1,10):
            print "(" + str(x) + "," + str(y) + ")"

## while loop

    while button_not_pressed:
         drive()

# Python OOP

## class in Python

    class User:
        name = ""

        def __init__(self, name):
            self.name = name

        def sayHello(self):
            print "Hello, my name is " + self.name

    # create virtual objects
    james = User("James")
    david = User("David")
    eric = User("Eric")

    # call methods owned by virtual objects
    james.sayHello()
    david.sayHello()

## inheritance

    class User:
        name = ""

        def __init__(self, name):
            self.name = name

        def printName(self):
            print "Name  = " + self.name

    class Programmer(User):
        def __init__(self, name):
            self.name = name

        def doPython(self):
            print "Programming Python"

    brian = User("brian")
    brian.printName()

    diana = Programmer("Diana")
    diana.printName()
    diana.doPython()

## polymorphism

    class Bear(object):
    def sound(self):
        print "Groarrr"

    class Dog(object):
    def sound(self):
        print "Woof woof!"

    def makeSound(animalType):
    animalType.sound()

    bearObj = Bear()
    dogObj = Dog()

    makeSound(bearObj)
    makeSound(dogObj)

## polymorphism with abstract class

    class Document:
        def __init__(self, name):
            self.name = name

        def show(self):
            raise NotImplementedError("Subclass must implement abstract method")

    class Pdf(Document):
        def show(self):
            return 'Show pdf contents!'

    class Word(Document):
        def show(self):
            return 'Show word contents!'

    documents = [Pdf('Document1'),
                 Pdf('Document2'),
                 Word('Document3')]

    for document in documents:
        print document.name + ': ' + document.show()

Output:

    Document1: Show pdf contents!
    Document2: Show pdf contents!
    Document3: Show word contents!

## another example 

of abstract class:

    class Car:
        def __init__(self, name):
            self.name = name

        def drive(self):
            raise NotImplementedError("Subclass must implement abstract method")

        def stop(self):
            raise NotImplementedError("Subclass must implement abstract method")

    class Sportscar(Car):
        def drive(self):
            return 'Sportscar driving!'

        def stop(self):
            return 'Sportscar breaking!'

    class Truck(Car):
        def drive(self):
            return 'Truck driving slowly because heavily loaded.'

        def stop(self):
            return 'Truck breaking!'


    cars = [Truck('Bananatruck'),
            Truck('Orangetruck'),
            Sportscar('Z3')]

    for car in cars:
        print car.name + ': ' + car.drive()

Output:

    Bananatruck: Truck driving slowly because heavily loaded.
    Orangetruck: Truck driving slowly because heavily loaded.
    Z3: Sportscar driving!

Reference: [Python Beginner by pythonspot.com](https://pythonspot.com/beginner/)

# Python tricks

## start a simple HTTP server:

    python -m SimpleHTTPServer

## Using Zip 

to combine arrays

    >>> b = [[1, 2, 3, 4], [6, 5, 4, 3]]
    >>> zip(*b)
    [(1, 6), (2, 5), (3, 4), (4, 3)]

## We know that "array.reverse()" will reverse an array. 

How do we reverse a string?

    >>> s = "Hello world"
    >>> s = s[::-1]
    >>> print s
    dlrow olleH

## Swapping variables

    >>> a = 1
    >>> b = 3
    >>> b,a = a,b
    >>> print a
    3
    >>> print b
    1

Reference: [Fun tricks with Python, pythonspot.com](https://pythonspot.com/fun-tricks-with-python/)
