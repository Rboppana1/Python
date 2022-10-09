"""
Instructions
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
https://en.wikipedia.org/wiki/Prime_number
You need to write a function that checks whether if the number passed into it is a prime number or not.
e.g. 2 is a prime number because it's only divisible by 1 and 2.
But 4 is not a prime number because you can divide it by 1, 2 or 4.
Here are the numbers up to 100, prime numbers are highlighted in yellow:
Example Input 1
73
Example Output 1
It's a prime number.
Example Input 2
75
Example Output 2
It's not a prime number.
Hint
Remember the modulus:
https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
Make sure you name your function/parameters the same as when it's called on the last line of code.
Use the same wording as the Example Outputs to make sure the tests pass.
"""
# Write your code below this line 👇

def prime_checker(number):
    for i in range(2, number):
        if (number % i) == 0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
