# All types of iterations in one simple Python code

# 1. For loop with range
print("1. For loop with range:")
for i in range(1, 4):
    print("  For loop:", i)

# 2. While loop
print("\n2. While loop:")
i = 1
while i <= 3:
    print("  While loop:", i)
    i += 1

# 3. Loop through a list
print("\n3. Looping through a list:")
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    print("  Animal:", animal)

# 4. Loop through a string
print("\n4. Looping through a string:")
for char in "Hi":
    print("  Char:", char)

# 5. Using enumerate
print("\n5. Using enumerate:")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"  Color {index}:", color)

# 6. Using break and continue
print("\n6. Break and continue in loop:")
for i in range(1, 6):
    if i == 2:
        continue  # skip 2
    if i == 4:
        break     # stop before 4
    print("  Value:", i)