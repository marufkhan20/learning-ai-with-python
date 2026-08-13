# 1. Accept a integer and Print Hello world n times - Solved
# num = int(input("Enter your number "))

# for i in range(num):
#     print("Hello World")

# 2. Print natural number Up to n - Solved
# num = int(input("Please enter your number "))

# for i in range(1, num+1):
#     print(i)

# 3. Reverse for loop, Print n to 1 - Solved
# num = int(input("Please enter your number "))

# for i in range(num, 0, -1):
#     print(i)

# 4. Take a number as input and print it's table - Solved
# num = int(input("Please enter your table num "))

# for i in range(num, num * 10 + 1, num):
#     print(i)

# 5. Sum up to n terms - Solved
# num = int(input("Enter your number "))

# total = 0

# for i in range(1, num +1):
#     total += i

# print(f"Total: {total}")

# 6. Factorial of a number - Solved
# num = int(input("please enter your number "))

# factorial = 1

# for i in range(1, num + 1):
#     factorial *= i

# print(factorial)

# 7. Print the sum of all even & odd number in a range seperately - Solved
# num = int(input("Enter your number "))

# evenSum = 0
# oddSum = 0

# for i in range(1, num + 1):
#     if i % 2 == 0:
#         evenSum += i
#     else:
#         oddSum += i

# print(f"Even Sum is: {evenSum}")
# print(f"Odd Sum is: {oddSum}")

# 8. Print all the factors of a number - Solved
# num = int(input("Enter your number - "))

# for i in range(1, num + 1):
#     if num % i == 0:
#         print(f"Factor is - {i}")

# 9. Accept a number and check if it a perfect number or not - Solved
# num = int(input("Enter your number - "))

# sum = 0

# for i in range(1, num):
#     if num % i == 0:
#         print(i)
#         sum += i

# if (sum == num):
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")

# 10. Check wether number is prime or not - Solved
# num = int(input("Enter your number "))

# primeLength = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         primeLength += 1

# if primeLength == 2:
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not a prime number")

# 11. Reverse a string without inbuild function - Solved
# str = "MARUF"

# reverseStr = ""

# for i in range(len(str)):
#     reverseStr += str[len(str) - 1- i]

# print(reverseStr)

# 12. check string is Pallindrom or not - Solved
# str = input("Enter your String - ")

# reverseStr = ""

# for i in range(len(str)):
#     reverseStr += str[len(str) - 1- i]

# if str == reverseStr:
#     print(f"{str} is a Pallindrom")
# else:
#     print(f"{str} is not a Pallindrom")

# 13. Count all latters, digit and special symbols from given string
