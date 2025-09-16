# ✅ Task 1 – Reverse a String
word = "Yezdi"
reversed_word = word[::-1]
print("Reversed string:", reversed_word)

# ✅ Task 2 – Split and Find
sentence = ("Made for Motorcycling")
words_list = sentence.split()
print("Words list:", words_list)
word = ("World")
position = word.find("W")
print(position)

# ✅ Task 3 – Join a List of Words
list = ["Python", "is", "fun"]
joinedsentence = " ".join(list)
print("\nJoined sentence:", joinedsentence)

# ✅ Task 4 – Data Type Check and Conversion
a = 10
print("type of a :", type(a))
b= 10.1
print("type of b :",type(b))
c = "Adventure"
print("type of c :",type(c))
d = False
print("type of d :",type(d))
e = int(b)
print(e)
f = float(a)
print(f)

# ✅ Task 5 – Combined Challenge
colors_input = "Red,Blue,Yellow,Green"  
colors_list = colors_input.split(",")   
print("Result:", colors_list)
colors_list.reverse()                   
reversed_colors = ",".join(colors_list) 
print("Reversed colors string:", reversed_colors)

