# Question no:1
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Question no:2
a = 10           
b = 3.14         
c = "Hello"      
d = True         

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

num_int = 25
num_str = str(num_int)    
print("Converted int to string:", num_str, type(num_str))

num_float = 12.7
num_int2 = int(num_float) 
print("Converted float to int:", num_int2, type(num_int2))

# Question no:3
# Implicit conversion
x = 5       
y = 2.5     
z = x + y   
print("Result:", z, "Type:", type(z))

# Explicit conversion
s = "123"
num = int(s) * 2
print("Explicit conversion result:", num, "Type:", type(num))

# Qusetion no:4
x = 10
print("Initial x:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x //= 2
print("After //= 2:", x)

x %= 3
print("After %= 3:", x)

# Question no:5
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)
print("Power:", a ** b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("a == b:", a == b)
print("a != b:", a != b)
