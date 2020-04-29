# from functools import cmp_to_key


# Please write the "renderPerson" function required to print a string like the following:

# Bob is a 23 years old male born in 05/22/1983 with green eyes

# Hint: You have to do some string concatenation and return that string.

def renderPerson(name, dob, age, gender, eyecolor):
    return name + ' is a ' + age + ' year-old ' + gender + ' born in ' + dob + ' with ' + eyecolor + ' eyes.'


name = 'Paula'
dob = '09/22/1986'
age = '33'
gender = 'female'
eyecolor = 'brown'

# x = name + ' is a ' + age + ' year-old ' + gender + ' born in ' + dob + ' with ' + eyecolor + ' eyes.'

print(renderPerson(name, dob, age, gender, eyecolor))

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

# For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.

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
# elif total <= 50:
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

def isOdd(x):
    return x % 2 == 1

print(isOdd(45346))
print(isOdd(45345))

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