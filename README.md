# Tech Intern test 

This repository was developed as a solution to the challenge proposed for the Thech Intern selection process. In this repository you will see a way to develop the 'Palindromes' exercise. Stay a while and see how the development process went.

### Why this exercise?

Sometimes, as challenging as it may seem, taking a risk can bring great learning. This is one of those challenges that I wanted to learn from and put my skills into practice, as well as have fun in the process.

## The development process

What is this exercise about? Here is the statement:

"You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 0's left of all higher digits in your tests. For example 0110 is valid, 0011 is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the constraints."

First of all, what is a 'palindrome'?

![Palindrome](https://t3.ftcdn.net/jpg/03/20/25/00/360_F_320250061_pPaPUOxre35RFq8mnCZFDjPgguPJzsLe.jpg)

A palindrome is a word, sentence, verse, or even number that reads the same backward or forward. It derives from Greek roots that literally mean “running back” (palin is “again, back,” and dromos, “running.”).

The first step in performing this exercise was to check that the arguments received were of the correct type. Once it was verified, it was important to determine which was the pattern that determined the minimum number of changes that must be made in a given number to convert it into a palindrome. This in order to be able to determine in which cases it was possible to proceed and in which cases '-1' was returned.

After performing all the checks, I proceeded to alter the string to make it palindromic, first with the minimum number of changes, and then, if further changes were still possible, to replace strategic numbers to create a combination that results in the highest possible number.

Et voilà!

## How this works

This function takes three arguments: 
- An n-digit dtring of numbers.
- Two integers, n and k, the number of digits in the number and the maximum numbers of changes allowed.

And you will obtain the following:

Sample input
```
higest_value_palindrome("092282", 6, 4)
```

Sample output
```
992299
```

### How to use this code

First, clone this rebo by using:
```
git clone https://github.com/abimont/test-tech_intern-tul.git
```

Edit the ```main.py``` file to test your own numbers, or create a new file and import the function by using:
```
higest_value_palindrome = __import__('higest_value_palindrome').higest_value_palindrome
```

Now you will be able to use the function as you saw in the previous example.

### Credits

This repository was developed by [Abigail Montes](https://www.linkedin.com/in/abi-dev)

