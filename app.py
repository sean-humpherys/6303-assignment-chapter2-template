# Chapter 2.1 Variables

import math
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(students_count)

# Chapter 2.2 Variable Names

students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"

# Chapter 2.3 Strings

course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# Chapter 2.4 Escape Sequences
# \"
course = "Python \"Programming"
print(course)
# \'
course = "Python \'Programming"
print(course)
# \\
course = "Python \\Programming"
print(course)

# Chapter 2.5 Formatted Strings

first = "Sean"
last = "Humpherys"
full = f"{len(first)} {2 + 2}"
print(full)

# Chapter 2.6 String Methods

course = " python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

# Chapter 2.7 Numbers

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3

# Chapter 2.8 Working with Numbers


print(round(2.9))
print(abs(-2.0))

print(math.ceil(2.2))

# Chapter 2.9 Type Conversion

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

#ways to write False or values that evaluate to False
# False
# ""
# 0
# None


print("testing_" * 10)

