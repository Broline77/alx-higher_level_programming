# 0x13-javascript_objects_scopes_closures
## Resources
Read or watch:

- [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
- [Object-oriented JavaScript (read all examples!)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
- [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
- [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [this/self](https://alistapart.com/article/getoutbindingsituations/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What this means
- What undefined means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

# Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

# TASKS:

# TASK 0: Rectangle #0
Write an empty class Rectangle that defines a rectangle:

- You must use the class notation for defining your class

# TASK 1:  Rectangle #1
Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h

# TASK 2: Rectangle #2
Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object

# TASK 3: Rectangle #3
Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments: w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object
- Create an instance method called print() that prints the rectangle using the character X

# TASK 4: Rectangle #4
Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments: w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object
- Create an instance method called print() that prints the rectangle using the character X
- Create an instance method called rotate() that exchanges the width and the height of the rectangle
- Create an instance method called double() that multiples the width and the height of the rectangle by 2

# TASK 5: Square #0
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

- You must use the class notation for defining your class and extends
- The constructor must take 1 argument: size
- The constructor of Rectangle must be called (by using super())

# TASK 6: Square #1
Write a class Square that defines a square and inherits from Square of 5-square.js:

- You must use the class notation for defining your class and extends
- Create an instance method called charPrint(c) that prints the rectangle using the character c
  - If c is undefined, use the character X

# TASK 7: Occurrences
Write a function that returns the number of occurrences in a list:

- Prototype: exports.nbOccurences = function (list, searchElement)


# TASK 8: Esrever
Write a function that returns the reversed version of a list:

- Prototype: exports.esrever = function (list)
- You are not allow to use the built-in method reverse

# TASK 9: Log me
Write a function that prints the number of arguments already printed and the new argument value. (see example below)

- Prototype: exports.logMe = function (item)
- Output format: <number arguments already printed>: <current argument value>

# TASK 10: Number conversion
Write a function that converts a number from base 10 to another base passed as argument:

- Prototype: exports.converter = function (base)
- You are not allowed to import any file
- You are not allowed to declare any new variable (var, let, etc..)

