#Question -1
# print('hello world!')
# print('please enter your name?')
# myName = input()
# print('good to talk to you, '+ myName)
# print('the length of your name is '+str(len(myName)))
# print('what is your age? ')
# myAge = input()
# print('you will be ' +str(int(myAge) + 1) + ' next year')

#Question -2
# import math
# import os
# import random
# import re
# import sys
#
#
#
# if __name__ == '__main__':
#     n = int(input().strip() )
#     if n%2 ==0:
#         if n>=2 and n<=5 :
#             print('not weird')
#         elif n>=6  and n<=20:
#             print('weird')
#         elif n>20:
#             print('not weird')
#     elif n%3 ==0:
#         print('weird')
#     else:
#         print('Weird')

#Question-3
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(str(a+b))
#     print(str(a-b))
#     print(str(a*b))

#Question -4
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(str(int(a/b)))
#     print(str(float(a/b)))

#Question -5

# import random
#
# if __name__ == '__main__':
#     n = int(input())
#     new = 0
#     count = 0
#     while count < n:
#         count = count + 1
#     new = 0

#Question -6
#Write a function
# def is_leap(year):
#     leap = False
#     if (year) % 4 == 0:
#         if year % 100 != 0:
#             leap = True
#         elif year % 400 == 0:
#             leap = True
#     else:
#         leap = False
#     # Write your logic here
#
#     return leap
#
#
# year = int(input())
#
# print(is_leap(year))