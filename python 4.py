# 1. Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

print("\n-------------------------------")

# 2. Marks to Grade
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

print("\n-------------------------------")

# 3. Leap Year Check
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

print("\n-------------------------------")

# 4. Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)       
print("x is not z:", x is not z)   

print("\n-------------------------------")

# 5. Membership Operator
word = "apple"
if "a" in word:
    print("'a' is present in", word)
else:
    print("'a' is not present in", word)

print("\n-------------------------------")
# 6. Bitwise AND, OR, XOR
a = 5   # binary 0101
b = 3   # binary 0011
print("5 & 3 =", a & b)   
print("5 | 3 =", a | b)   
print("5 ^ 3 =", a ^ b)   

print("\n-------------------------------")

# 7. Bitwise NOT
num = 6
print("~6 =", ~num)   # -7

print("\n-------------------------------")
# 8. Left and Right Shift
print("4 << 2 =", 4 << 2)    
print("16 >> 2 =", 16 >> 2)  
