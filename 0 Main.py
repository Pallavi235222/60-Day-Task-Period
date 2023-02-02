# Drawing a shape
'''
print("     /|")
print("   /  |")
print(" /    |")
print("/__ | ")

# variables 

# creating variables

character_name = "pallavi"
character_age= "19" 
print("there once was a woman named " + character_name + ",")
print("She was " + character_age + " years old.")

character_name = "yashu"
print("She really liked the name " + character_name + ".")
print("but didn't like being " + character_age + ".")
'''
'''
# working with strings
phrase = "pall avi"
#print(phrase.isupper() )
#print(phrase.upper().isupper() )
#print(len(phrase))
#print(phrase[3])
#print(phrase.index("p"))
#print(phrase.replace("avi", "AVI"))

# working with numbers
#print(3 * (4+5))
#print(10%7)
my_num = 5
print(my_num)
# converting in to a string
my_num = 5
print(str(my_num) + " my favorite number")
#math functions
# abs
my_num = -5
#print(abs(my_num))
#  2 pices of information 
print(pow(3, 3))
print(max(3,7))
print(min(3,7))
print(round(3.7))

from math import *
print(floor(3.8))
print(ceil(3.8))
print(sqrt(39))

# get input from user
name = input("enter your name: ")
age = input("enter your age: ")
print("hello " + name + "! you are " + age) 

#basic calculator
num1 = input("enter a number: ")
num2 = input("enter another number: ")
result = int(num1) + int(num2)

print(result)

#Mad libs Game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")


print("Roses are " + color)
print( plural_noun + " are blue")
print("I love " + celebrity)

#LIST
friends = ["pallavi","yashu","kalyan", "vandhana"]
friends[2] = "abi"
#print(friends)
print(friends[2])
#print(friends[1:2])


#LIST FUNCTIONS
lucky_numbers = [4,5,6,8,2,90,]
friends = ["pallavi", "pallavi","yashu","kalyan", "vandhana ","abi"]
#friends.extend(lucky_numbers)
#friends.append("vandhana") O/P: ['pallavi', 'yashu', 'kalyan', 'vandhana ', 'abi', 'vandhana']
#friends.insert(1,"darshan") O/P: ['pallavi', 'darshan', 'yashu', 'kalyan', 'vandhana ', 'abi']
#friends.remove("abi")
#friends.clear()
#friends.pop()
#friends.sort()
#lucky_numbers.sort()
#lucky_numbers.reverse()
#friends2 = friends.copy()
#print(friends2)
#print(lucky_numbers)
#print(friends.index("yashu"))
#print(friends.count("pallavi"))


#TUPLES
coordinates = (4, 5)
print(coordinates[1])

#FUNCTIONS
#creating function
def sayhi():
    print("hello user")
    
sayhi()

#giving parameters
def sayhi(name):
    print("hello " + name)
    
sayhi("Pallu")
sayhi("yashu")


#RETURN STATEMENTS
def cube(num):
    return num*num*num
    
print(cube(3))

# creating variable
def cube(num):
    return num*num*num
    
result = cube(3)
print(result)

#If STATEMENTS

is_male = False
is_tall = False
# using OR operator
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are not a male")
    
# using AND operator
is_male = True
is_tall = True
if is_male and is_tall:
    print("you are a male")
else:
    print("you are not a male or male or not tall or both")
'''
is_male = False
is_tall = False
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are not a male or male or not tall or both")