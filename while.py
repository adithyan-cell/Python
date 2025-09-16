i = 10
while i>=1:
    print(i)
    i=i-1 

    num = int(input("Enter a number: "))
i = 1
while i<=10:
    print(num,"x",i,"=",num*i)
    i = i+1

    num = int(input("Enter the values: "))
sum = 0
i = 1
while i<=num:
    sum = sum+i
    i = i+1
print("\n Sum = ",sum)

i =0
while i==0:
    print(i)

    num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit =temp % 10
    sum+= digit**len(str(num))
    temp //= 10
if num ==sum :
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

    i =1 
while i<=5:
    j =1
    while j <= 10:
        print(j,end = "")
        j =j+1
    i +=1
    print()

    for i in range(5):
    for j in range(1,11,1):
        print(j,end = "")
    print()  

    string = input("Please enter your word: ")
char = input("Please enter your character: ")
i = 0
count = 0
while(i < len(string)):
    if(string[i] == char):
        count = count+1
    i = i+1
print("The total number of Timer",char,"has occured = ",count)        