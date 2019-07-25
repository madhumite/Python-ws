'''7.	Write a program to find the sum of squares of only the even numbers in the given list. (Hint: Use the methods filter, map, reduce.)
Example:
Input:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Output:
Sum of squares of even numbers = 120
'''
from functools import reduce
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reduce(lambda a,b:a + b,map(lambda x:x ** 2,filter(lambda x:x % 2 == 0,list))))