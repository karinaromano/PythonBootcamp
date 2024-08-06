bmi = 84 / 1.65 ** 2

print(int(bmi))

print(round(bmi)) # to rounded to next whole number

print(round(bmi, 2)) # rounded with 2 decimals

#Assignment Operator
score = 0

#User scores a point
score += 1 # you can use -= ; *= : /=
print(score)

#f-strings
print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

#Which of these lines of code will give you an error?
name = input("What is your name?")
print(f"Hello, {name}")

name = input("What is your name?")
print("Hello, " + name)

age = 12
print(f"You are {age} years old")

age = 12
print("You are " + str(age) + " years old")

#age = 12
#print("You are " + age + " years old") # can only concatenate str (not "int") to str
