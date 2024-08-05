# Data Types, Numbers, Operations, Type Conversion and f-Strings
# Build a tip calculator

#lenght function to know how many characters the string has
print(len("Hello"))

#Data Types
#String
#Integers
#Floats
#Booleans

#Subscripting
print("Hello"[0]) # programmers always start counting from zero and also counts the space
#This method of pulling out a particular element from a string is called #subscripting


print("Hello"[4]) #
print("hello"[-1]) #negative indices -1 last character
print("Hello"[-2]) # from the end to the beginning <-

#123 is treated as a number
#"123" is treated as any other piece of text

#String
print("123" + "345") # Concatenation

#Integer = whole number -. write the number without anything else
print(123 + 345)

#Large Integers -> for large numbers we use to put commas
print(123_456_789) #in python we use Underscore _ between large numbers more readable,
#but the computer will treat as a whole large number and ignores the underscore

#Float = Floating point number (Decimal places)
print(3.14159)

#Boolean = True or False
print(True)
print(False)
#Booleans don't have quotation marks around them,
# otherwise it would turn them into a String. So it should be bool = False

# print(len(123456)) #TypeError: object of type 'int' has no len()
print(len("Hello"))

#How would we know what is the Data Type fo "Hello"?
#Function => type("Hello") => for type checking
type("Hello")
print(type("Hello")) # <class 'str'>
print(type(123456)) # <class 'int'>

#Practice
# using type and print functions to print out 4 lines into
# the output area so we get the full collection of data type
print(type("Karina")) #<class 'str'>
print(type(8061979)) #<class 'int'>
print(type(123.918)) #<class 'float'>
print(type(True)) #<class 'bool'> True or False with Capital T or F

#Type Conversion also knowing as Type Casting
"123" #this is a string but I want to convert to a number:
int("123")
print(int("123")) #123
print(int("123") + int("456")) #579

int()
float()
str()
bool()

#Practice
#make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))

name_of_the_user = input("Enter your name")
lenght_of_name = len(name_of_the_user)

#print(type("Number of letters in your name: ")) #str
#print(type(lenght_of_name)) #int

print("Number of letters in your name: " + str(lenght_of_name))

