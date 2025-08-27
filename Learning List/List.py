# Working with Python Lists

# Example 1: Creating and printing a list
marks = [12, 45, 67, 54, 89, 74]
print("Marks:", marks)

# Check type of variable
print("Type of marks:", type(marks))

# Length of the list
print("Length:", len(marks))

# Append a new element
marks.append(122)
print("After appending:", marks)


# Example 2: Updating elements in a list
student = ["Nauman Tariq", 18, "FSD"]
print("Student:", student)

# Update age
student[1] = 20
print("Updated student:", student)


# Example 3: Sorting lists
a = [12, 56, 86, 0]
a.sort()
print("Sorted ascending:", a)

a.sort(reverse=True)
print("Sorted descending:", a)


# Example 4: Removing and inserting
b = [12, 67, 89, 76, 45]
b.pop(1)   # Remove element at index 1
print("After pop:", b)

b.insert(1, 99)  # Insert at index 1
print("After insert:", b)


# Example 5: Taking input for list of languages
languages = []
lang1 = input("Enter 1st language: ")
lang2 = input("Enter 2nd language: ")
lang3 = input("Enter 3rd language: ")
lang4 = input("Enter 4th language: ")

languages.append(lang1)
languages.append(lang2)
languages.append(lang3)
languages.append(lang4)

print("Languages entered:", languages)
