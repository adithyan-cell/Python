a = 5
b = 6
c = 0
if a and b and c:
    print("All the numbers have boolean values as True")
else:
    print("Atleast one number has boolean value as False")

a = 10
b = -10
c = 0
if a>0 or b>0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

a = 10
b = 12
c = 12
print(a!=b)
print(b!=c)
if a!=b:
    print(" a and b are different")
if a%2 != 0:
    print("Number is odd number" )
else:
    print("Number is even number")

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight/(height/100)**2
print("Your BMI is: ",BMI)
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=29.9:
    print("You are overweight")
elif BMI<=34.9:
    print("You are severely overweight")
elif BMI<=39.9:
    print("You are obese")
else:
    print("You are severely obese")