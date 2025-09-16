print("Select your choice")
print("1.Two wheeler")
print("2.Car")
choice1 = int(input("Enter your choice: "))
if(choice1==1) :
    print("What type of Two wheeler?")
    print("1.Bike\n")
    print("2.Scooter\n")
    
    choice2 = int(input("Enter your choice: "))
    if(choice2==1) :
        print("You have selected bike")
    else:
        print("You have selected scooter")
elif(choice1==2):
    print("What type of Car")
    print("1.Hatchback\n")
    print("2.Sedan\n")
    print("3.SUV\n")
    
    choice3 = int(input("Enter your choice: "))
    if(choice3==1):
        print("You have selected Hatchback")
    elif(choice3==2):
        print("You have selected Sedan")
    else:
        print("You have selected SUV")
        
else:
    print("Wrong choice")