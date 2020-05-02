# This loop is looping the array from beginning to end... increasing one by one.

# Instructions
# Lets try looping from the end to the beginning.

numbers = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]


for i in reversed(numbers):
    print i


# Using the console.log function, print the 3rd item from the array.
# Change the value in the position where 'Thursday' is located to null.
# Print that particular position.

# Important note: Use null as a value and not "null" as a string.

# weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
# weekdays[0] = 'Thursday'

# print(weekdays[0])

# print(weekdays[0])



# Define a procedure, print_numbers, that takes as input a positive whole number and prints out all the whole numbers from 1 to the input 

# i = 0


# def print_numbers(number):
#   i = 0
#   while i != number:
#     i = i + 1
#     print (i)
  
# print_numbers(5)



#Write the same is_friend function except now the friend names start with D or N

# def is_friend(name):
#   return name[0] == 'D' or name[0] == 'N'

# # def is_friend(name):
# #   if name[0] == 'D':
# #     return True
# #   if name[0] == 'N':
# #     return True
# #   else:
# #     return False
# #     return False

# print(is_friend('Diego'))
# print(is_friend('Canu'))
# print(is_friend('Nancy'))


#Write a function called if_friend that takes a string as its input, and outputs a Boolean indicating if the input string is the name of a friend. Assume I am friends with anyonoe whose name starts with a D and no open

# def if_friend(x):
#   if x[0] == 'D':
#     return 'Yes'
  
#   return 'No'

# print(if_friend('damian'))

#another way is to just return the expression

# def is_friend(name):
#   return name[0] == 'D'

# print(is_friend('Daniel'))


# print(5 == '5')


# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find, or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

# text = """Wow this is a fairly long body of text. Quite a few characters too.
# I wonder if the string.find method could help find where NOUN is located.
# That way, I could go out and VERB with my friends rather than counting characters
# all day long!"""

# noun_position = text.find('NOUN')
# verb_position = text.find('VERB')


# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

# sentence = 'A NOUN went on a walk. It can VERB really fast.'

# substring1 = sentence[:2]
# substring2 = sentence[6:sentence.find('VERB')]
# substring3 = sentence[34:]

# noun_replacement = 'culo'
# verb_replacement = 'poop'

# new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3

# print(new_sentence)

# print

# print(substring2)

# print(substring1)


#Given the variables s and t defined as:

# s = 'udacity'
# t = 'bodacious'

# # write Python code that prints out udacious without using any quote characters in your code

# print(s[0] + t[2:])




# s = 'Paunu is awesome'

# print(s[0] + s[1])

# print('a' + s)[1:]

# print(('a'+s)[1:])

# print(s[0] + s[1:]) # doesn't work if s = ''

# print(s + '')

# print(s[0:])



# print "Example 3: Printing out everything after a certain substring"

# my_string = 'My favorite color: blue'
# color_start_location = my_string.find('color:')
# favorite_color = my_string[color_start_location:]

# print(favorite_color)
# print(favorite_color[7:])




# s = 'any string'

# # print(s + s[0:-1+1])

# # print(s + s)

# print(s.find(s + '!!!') + 1)

#Write a code that defines the variable age to be your age in years, and then prints out the number of days you have been alive

# age = 33
# days_in_year = 365 

# days_alive = age * days_in_year

# print(days_alive)


# Print out the distance, in meters, that light travels in one processing cycle

# speed_of_light = 299792458 # meters per second
# cycles_per_second = 2800000000. # 2.8Ghz

# cycle_distance = speed_of_light / cycles_per_second

# # print(speed_of_light * (1/cycles_per_second))
# print (cycle_distance)

# Write a JavaScript function called "nonRepeated" to find the first not repeated character.

# def nonRepeated (str1):


# write a function that makes the square of a number

# def square(x):
#   return x * x

# print (square(5))


# Write a JavaScript function called "nonRepeated" to find the first not repeated character.

# print 2 + 2

# def nonRepeated():
  


# first_word = 'hello'
# second_word = 'world'

# # sentence = first_word + ' ' + second_word + '!'

# print(f'{first_word} {second_word}')


# Write a function called sortNames that, given an array of names, returns them in alphabetical order.

# def sortNames (lst_names):
#   return sort(lst_names)

# names = ['Paunu', 'Luis', 'Pepe', 'Peps', 'Canu', 'Valerain']

# names.sort(reverse=True)

# print(names)



# def sortNames (a, b):
#   if a > b:
#     print(b,a)
#   else:
#     return(a,b)

# sortNames('Paunu', 'Paula')









# name = 'Paula'
# dob = '09/22/1986'
# age = '33'
# gender = 'female'
# eyecolor = 'brown'

# x = name + ' is a ' + age + ' year-old ' + gender + ' born in ' + dob + ' with ' + eyecolor + ' eyes.'

# # print(renderPerson(name, dob, age, gender, eyecolor))

# print(x)


# total = 105

# if total > 100:
#     print('Give me your money!')
# elif total > 50:
#     print ('Buy me some coffee you cheap!')
# elif total <= 50:
#     print ('You are poor, go away')



# from functools import cmp_to_key


# Please write the "renderPerson" function required to print a string like the following:

# Bob is a 23 years old male born in 05/22/1983 with green eyes

# Hint: You have to do some string concatenation and return that string.

# def renderPerson(name, dob, age, gender, eyecolor):
#     return name + ' is a ' + age + ' year-old ' + gender + ' born in ' + dob + ' with ' + eyecolor + ' eyes.'


# name = 'Paula'
# dob = '09/22/1986'
# age = '33'
# gender = 'female'
# eyecolor = 'brown'

# # x = name + ' is a ' + age + ' year-old ' + gender + ' born in ' + dob + ' with ' + eyecolor + ' eyes.'

# print(renderPerson(name, dob, age, gender, eyecolor))

# print(x)



# Is a very good practice that all functions return something, even if it is "null"; if your functions return something you can then create algorithms that use several functions at the same time. For example, in this particular case we have two functions available:

# dollarToEuro: that calculates the value in euros of a given value in dollars.
# autoToYen: calculates the value in yen of a given value in euros. Using the two functions available, calculate the value of 137 dollars in yen.


# def euro(x):
#     return x * 0.89

# def yen(x):
#     return x * 124.15

# dollar_to_euro = euro(137)

# euro_to_yen = yen(121.93)

# dollar_to_yen = yen(dollar_to_euro)

# print(dollar_to_yen)


# function - Using the squareArea function, print on the console the area of the following figures:

# def calculateArea(length, edge):
#     return length * edge

# squareArea = calculateArea(5,5)

# print(squareArea)


#function Please calculate the sum between 3445324 and 53454423 and assign the result to a variable called "superduper"

# def sum(number1, number2):
#     return number1 + number2

# superduper = sum(3445324, 53454423)

# print(superduper)


#Please write an algorithm that prompts the user for the number of people attending their wedding and prints the corresponding price in the console.

# For example, if the user says that 20 people are attending the wedding, it must cost $4,000 dollars.

# number_guests = input('How many people are coming to your wedding? ')

# # price = '90'

# if number_guests <= 50:
#     price = '$4000'
# elif number_guests <= 100:
#     price = '$10000'
# elif number_guests <= 200:
#     price = '$15000'
# else:
#     price = '$20000'

# # print('Your wedding will cost ' + str(price) + ' dollars.')
# print('Your wedding will cost ' + (price) + ' dollars.')



# # If the user has more than $100, we answer: "Give me your money!"
# If the user has more than $50, we answer: "Buy me some coffee you cheap!"
# If the user has less or equal than $50, we answer: "You are a poor guy, go away!"
# total = 105

# if total > 100:
#     print('Give me your money!')
# elif total > 50:
#     print ('Buy me some coffee you cheap!')
# elif total <= 50: #I could also write else here
#     print ('You are poor, go away')


#The function addNumbers is supposed to return the sum of 2 given numbers, please complete the needed code inside of the function to make it behave as expected.

# def addNumbers(x,y):
#     return x + y 

# print(addNumbers(3,4))


#The function isOdd is defined at the beginning of the code, please call that function passing it the number 45345 and print the result on the console.

# def isOdd(x):
#     if x % 2 == 0: 
#         return False    
#     return True

#both of these functions determine whether a number is odd
# def isOdd(x):
#     return not x % 2 == 0
# def isOdd(x):
#     return x % 2 == 1

# print(isOdd(45346))
# print(isOdd(45345))

#mod % es lo que sobra, it's not division



#string concatenation

# first_word = 'hello'
# second_word = 'world'

# # sentence = first_word + ' ' + second_word + '!'

# print(f'{first_word} {second_word}')


# print(sentence)


# 1.4 Please add 10 years to the value of the age variable
# age = 0 
# age += 10 

# print(age)

# print ('hello peps')