"""
Name :Pawan tripathi
Enrollment number : 0157AL231147
Batch : 5 (MTF) - 2027
Batch Time : 10:30 AM

"""


# Basic If-else Problems:
# 1. Write a program to check whether a number is positive, negative,or zero.

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")                
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")    

# 2. Write a program to check whether a number is even or odd.

num = int(input("Enter an integer: "))              
if num % 2 == 0:
    print("The number is even.")    
else:
    print("The number is odd.")

# 3. Write a program to check whether a year is a leap year or not.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 4. Write a program to find the greatest of two numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))        
if num1 > num2:
    print(f"{num1} is greater than {num2}.")    
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print("Both numbers are equal.")

# 5. Write a program to check whether a person is eligible to vote (age>=18) or not.

age = int(input("Enter your age: "))
if age >= 18:           
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 6. Write a program to check whether a character is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in 'aeiou' and len(char) == 1:
    print(f"{char} is a vowel.")    
elif len(char) == 1 and char.isalpha():
    print(f"{char} is a consonant.")
else:
    print("Please enter a valid single alphabet character.")

# 7. Write a program to check if a number is divisible by 5.

num = int(input("Enter an integer: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5.")
else:
    print(f"{num} is not divisible by 5.")

# 8. Write a program to determine whether a given number is single-digit , two-digit, or more than two-digit number.

num = int(input("Enter an integer: "))
if 0 <= num < 10 or -10 < num <= 0:
    print("The number is a single-digit number.")
elif 10 <= abs(num) < 100:
    print("The number is a two-digit number.")
else:
    print("The number has more than two digits.")

# 9. Write a program to check whether a student has passed or failed (pass mark is 40).

marks = float(input("Enter your marks: "))
if marks >= 40:
    print("You have passed.")   
else:
    print("You have failed.")

# 10. Write a program to find whether the entered number is a multiple of both 3 and 7.

num = int(input("Enter an integer: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 3 and 7.")  
else:
    print(f"{num} is not a multiple of both 3 and 7.")

# -------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

# Ladder If & Nested If Problems:
# 1. Write a program to find the greatest among  three numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greatest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the greatest number.")
else:
    print(f"{num3} is the greatest number.")

# 2. Write a program to classify a person based on age: Child (<13), Teen (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter your age: "))
if age < 13:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teen.")
elif 20 <= age <= 59:
    print("You are an Adult.")
else:
    print("You are a Senior.")

# 3. Write a program to assign gtades based on marks: A (90-100), B (75-89), C (50-74), D (35-49), Fail (<35).

marks = float(input("Enter your marks: "))
if 90 <= marks <= 100:
    print("Grade: A")       
elif 75 <= marks < 90:
    print("Grade: B")
elif 50 <= marks < 75:
    print("Grade: C")
elif 35 <= marks < 50:
    print("Grade: D")
elif 0 <= marks < 35:
    print("Grade: Fail")
else:
    print("Please enter valid marks between 0 and 100.")

# 4. Write a program to check the type of triangle (equilateral, isosceles, scalene) based on the lengths of its sides.
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))       
side3 = float(input("Enter length of third side: "))
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Please enter valid positive lengths for the sides.")
elif side1 == side2 == side3:
    print("The triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")

# 5. Write a program to chck is character is uppercase or lowercase or digit or special character.

char = input("Enter a character: ")
if len(char) != 1:
    print("Please enter a single character.")
elif char.isupper():
    print(f"{char} is an uppercase letter.")
elif char.islower():
    print(f"{char} is a lowercase letter.")
elif char.isdigit():
    print(f"{char} is a digit.")
else:
    print(f"{char} is a special character.")

# 6. Write a program to calculate electricity bill bsed on units:Upto 100 units: Rs. 5/unit, 101-200 units: Rs. 7/unit, Above 200 units: Rs. 10/unit.

units = float(input("Enter the number of units consumed: "))
if units < 0:
    print("Please enter a valid number of units.")
elif units <= 100:
    bill = units * 5
    print(f"Your electricity bill is: Rs. {bill}")
elif 101 <= units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    print(f"Your electricity bill is: Rs. {bill}")  
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    print(f"Your electricity bill is: Rs. {bill}")

# 7. Write a program to determine the largest of four nnumbers using nested if.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

if num1 >= num2:
    if num1 >= num3:
        if num1 >= num4:
            largest = num1
        else:
            largest = num4
    else:
        if num3 >= num4:
            largest = num3
        else:
            largest = num4
else:
    if num2 >= num3:
        if num2 >= num4:
            largest = num2
        else:
            largest = num4
    else:
        if num3 >= num4:
            largest = num3
        else:
            largest = num4
print(f"The largest number is: {largest}")


# 8. Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter a year: "))
if year % 100 == 0:
    if (year % 400 == 0):
        print(f"{year} is a century year and a leap year.")
    else:
        print(f"{year} is a century year but not a leap year.")
else:
    print(f"{year} is not a century year.")
    if (year % 4 == 0 and year % 100 != 0): 
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")    
        
# 9. Write a prgram to classify BMI value : Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obesity (30+).
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
if height <= 0:
    print("Please enter a valid height.")
else:
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are Underweight.")
    elif 18.5 <= bmi < 25:
        print("You have a Normal weight.")
    elif 25 <= bmi < 30:
        print("You are Overweight.")
    else:
        print("You are Obese.")

# 10. Write a program to display the smallest number among three numbers using nested if.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))   
num3 = float(input("Enter third number: "))
if num1 <= num2:
    if num1 <= num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 <= num3:
        smallest = num2
    else:
        smallest = num3
print(f"The smallest number is: {smallest}")

# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# For Loop Problems:
# 1. write a program using a for loop to print all the armstrong numbers between 100 and 999.
for num in range(100, 1000):
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
    if sum_of_cubes == num:
        print(num)
    else:
        continue

# 2. Write a program to generate and display the first n prime numbers using a for loop.

n = int(input("Enter how many prime numbers you want: "))
count = 0      
num = 2        
print(f"The first {n} prime numbers are:")

for num in range(2, 10000):  
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1
        if count == n:  
            break

# 3. Write a program to display all the numbers from 1 to 500 that are divisible by 3 , but the sum of their digits should not exceed 10.

for num in range(1, 501):
    if num % 3 == 0:
        digit_sum = sum(int(digit) for digit in str(num))
        if digit_sum <= 10:
            print(num)  
        else:
            continue
    else:
        continue

# 4. Write a program using for loop to print a pyramid of stars (*) of height n.Example for n=4.

n = int(input("Enter the height of the pyramid: ")) 
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))    


#5. Write a program to accept a **string** and check whether it is a **pangram** (contains all 26 alphabets at least once) using a for loop.  

s = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True
for ch in alphabet:
    if ch not in s:
        is_pangram = False
        break

if is_pangram:
    print("Pangram")
else:
    print("Not a Pangram")

#6. Write a program using a for loop to **print all twin primes between 1 and 100**.Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)).  
for i in range(2, 100):
    # check if i is prime
    is_prime_i = True
    if i < 2:
        is_prime_i = False
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime_i = False
                break

    # check if i+2 is prime
    is_prime_i2 = True
    if i + 2 < 2:
        is_prime_i2 = False
    else:
        for j in range(2, int((i + 2) ** 0.5) + 1):
            if (i + 2) % j == 0:
                is_prime_i2 = False
                break

    if is_prime_i and is_prime_i2:
        print(f"({i}, {i+2})", end=" ")


#7. Write a program that accepts a number from the user and prints whether it is a **Harshad number**  (a number divisible by the sum of its digits) using a for loop.  
n = int(input("Enter a number: "))
digit_sum = sum(int(d) for d in str(n))

if n % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")

#8. Write a program to generate **Pascal’s Triangle** up to `n` rows using a for loop.  
n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i), end="")
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

#9. Write a program using a for loop to display the **sum of the series**:  
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
    total += i ** 2
print("Sum of series =", total)

# 10. Write a program that accepts a number from the user and prints whether it is a **Strong number**  (sum of factorials of digits = number itself). Example: 145 → 1! + 4! + 5! = 145.  
import math

n = int(input("Enter a number: "))
s = sum(math.factorial(int(d)) for d in str(n))

if n == s:
    print("Strong Number")
else:
    print("Not a Strong Number")

# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------


# While Loop Problems:

# 11.Write a program using a while loop to find the reverse of a number and check if the reversed number is prime.Example: Input = 73 → Reverse = 37 → Prime.
n = int(input("Enter a number: "))

rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

is_prime = True
if rev < 2:
    is_prime = False
else:
    for i in range(2, int(rev ** 0.5) + 1):
        if rev % i == 0:
            is_prime = False
            break

print(f"Reverse = {rev}")
print("Prime" if is_prime else "Not Prime")

# 12.Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
total_digit_sum = 0
while total_digit_sum <= 100:
    n = int(input("Enter a number: "))
    total_digit_sum += sum(int(d) for d in str(n))

print("Stopped. Sum of digits exceeded 100.")

# 13.Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).
n = input("Enter a number: ")

if "0" in n and not n.startswith("0"):
    print("Duck Number")
else:
    print("Not a Duck Number")

# 14.Write a program using a while loop to accept a number and check if it is a Happy number.(A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1).Example: 19 is a happy number.
n = int(input("Enter a number: "))

seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(d) ** 2 for d in str(n))

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")


# 15.Write a program using a while loop to find the largest prime factor of a given number.
n = int(input("Enter a number: "))
i = 2
largest = 1

while n > 1:
    if n % i == 0:
        largest = i
        n //= i
    else:
        i += 1

print("Largest Prime Factor:", largest)

# 16.Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
while True:
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome entered. Stopping.")
        break

# 17.Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root).Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2.
n = int(input("Enter a number: "))

while n > 9:
    n = sum(int(d) for d in str(n))

print("Digital Root =", n)

# 18.Write a program using a while loop to generate the Collatz sequence for a given number.Rule: If n is even → n/2, if odd → 3n+1. Continue until n=1.
n = int(input("Enter a number: "))

print("Collatz sequence:")
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(1)

# 19.Write a program using a while loop to accept a number and check whether it is a Kaprekar number.(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.Example: 45² = 2025 → 20 + 25 = 45).
n = int(input("Enter a number: "))
sq = str(n ** 2)
right = int(sq[-len(str(n)):] or 0)
left = int(sq[:-len(str(n))] or 0)

if left + right == n:
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")

#20.Write a program to simulate an ATM machine using a while loop where a user can:
#       Check balance
#       Deposit money
#       Withdraw money (only if balance is sufficient)
#       Exit , Continue until the user chooses to exit.

balance = 0

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print("Balance =", balance)
    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print("Deposited:", amt)
    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient Balance")
    elif choice == 4:
        print("Exiting ATM. Goodbye!")
        break
    else:
        print("Invalid choice.")
