# dictionary is a built in data type
# dictionary is made up of key:value pairs
# keys are unique in a dictionary
# keys need to be immutable objects
# values can be of any type

grade_book = {'Fred': 99, 'Barney': 87, 'Wilma': 93}
print(grade_book)

print("Usig the items method in the dictionary class")
for item in grade_book.items():
    print(item)

for key, value in grade_book.items():
    print(key, value)

print("Using the keys method in the dictionary class")
for key in grade_book.keys():
    print(key)
for key in grade_book.keys():
    print(grade_book.get(key))

print("Using the values method in the dictionary class")
result = 0
for value in grade_book.values():
    result += value
average = result / len(grade_book)
print("average grade: " + str(average))
