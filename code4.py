#numerical no.01: finding age 
#solution:
def age(current_year , birth_year):
    return current_year - birth_year

current_year = 2024
your_birth_year = int(input("Enter your birth year: "))
print("Your age is ",age(current_year , your_birth_year))

print('_______________ \n')


#numerical no.02: area of rectangle: 
#solution:
def area(lenght , width):
    return lenght * width

lenght = int(input("Enter the Lenght of rectangle: "))
width = int(input("Enter the width of rectangle: "))
print("The area of your rectangle is " , area(lenght , width))
print('_______________ \n')


#numerical no.03 :area of circle ; pie*r^2
#solution:
def area_of_circle(radius):
    return (radius**2)*3.1417

radius = float(input("Enter the radius of circle: "))
print("The area of circle is " , area_of_circle(radius))
print('_______________ \n')


#numerical no.04: area of cube ; to find the area of cube use 6a^2
#solution:
def cube_area(surface_area):
    return 6 *(surface_area ** 2)

surface_area = float(input("Enter the surface area of cube: "))
print("The area of your cube is ", cube_area(surface_area))
print('_______________ \n')



#numerical no 05: conversion of temperature:
#solution:
def temp(farenhite):
    farenhite = (9/5)*(temperature + 32)
    return round(farenhite ,2 ) #here round function is used to display only 2 values after decimal point.

def temp(celsius):
    celsius = (5/9)*(temperature - 32)
    return round(celsius, 2)

user_temp = str(input("What type of conversion you're going to do? \n Choose 01 or 02  \n 01) Celsius to Fahrenheit \n 02) Fahrenheit to celsius? \n Your answer: "))
temperature = float(input("Enter temperature in numbers: "))
celsius = 0  
farenhite = 0
if user_temp == "01":
    print(f"{temperature} ﾟC in Fahrenheit = " , temp(farenhite) )
else :
    print(f"{temperature} ﾟF in Celsius = " , temp(celsius))

print('_______________ \n')



#numerical no 06 : time conversion_method 02
#solution:
def convert_seconds(seconds):
    minutes = seconds / 60
    hours = seconds /3600
    return minutes, hours

def convert_minutes(minutes):
    seconds = minutes*60
    hours = minutes/60
    return seconds ,hours

def convert_hours(hours):
    seconds = hours*3600
    minutes = hours *60
    return seconds ,minutes 

user_time = int(input("Which conversion do you want to perform? \n_________________ \n Choose any one option \n 1)seconds \n 2)minutes \n 3)hours \n Enter your answer in numbers: "))

time_value = int(input("Enter time: "))

if user_time ==1:
    minutes ,hours = convert_seconds(timevalue)
    print(f"{time_value} seconds is equals to {minutes} minutes and {hours} hours.")
elif user_time ==2:
    seconds , hours = convert_minutes(time_value)
    print(f"{time_value} minutes is equal to {seconds} seconds and {hours} hours.")
else:
    seconds , minutes = convert_hours(time_value)
    print(f"{time_value} hours is equals to {seconds} seconds and {minutes} minutes.")

print("__________________\n")

#numerical no 07 : % calculation
#solution:
def percentage(number,total_num):
    percent = int((number/total_num)*100)
    return percent

number = int(input("Enter your gained marks: "))
total_num = int(input("Enter total marks: "))
print(number , " = " , percentage(number , total_num),"%")

print('_______________ \n')

#numerical no 08:  Calculating BMI
#solution:
def bmi(weight,height):
    BMI = weight / (height**2)
    return round(BMI,2)

weight =float(input("Enter your weight in KG's : "))
height =float(input("Enter your height in meters: "))
body_mass_index = bmi(weight,height)
if body_mass_index < 18.5:
    print("You are under-weight \nTake healty diet :)")
elif 18.5 <= body_mass_index <= 24.9:
    print("Your weight is Normal. \nKeep up the good work 👍🏼")
elif 25 <= body_mass_index <=29.9 :
    print("You are over-weight. \nHit the Gym 💪🏼")
else :
    print("You are Obese! \nTake care of yourself before it's too late")

print('_______________ \n')


#numerical no 09 :calculating volume of cylinder
#solution:
print("To find the volume of cylinder : V = 3.1415*(radius^2)*height")
print("----------- \n ")

def cylinder(radius,height):
    volume = int(3.1415 *(radius**2)*height)
    return volume

radius = float(input("Enter th of radius of cylinder: "))
height = float(input("Enter the height of cylinder: "))
print("The volume of cylinder is ", cylinder(radius,height) , "cubic meter")

print('_______________ \n')

