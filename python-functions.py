#1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
    print(sum)

sum_to(6)

#2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  x = max(nums)
  print(x)

largest([25, 6, 70])

#3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(one, two):
  print(one.count(two))

occurrences('fleep floop', 'e')






