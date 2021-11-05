nums = [2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6, 6]
counts = {}

for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

max_count = 0
most_common = []

for key in counts.keys():
    if counts[key] > max_count:
        max_count = counts[key]
        most_common = [key]
    elif counts[key] == max_count:
        most_common.append(key)

print("Most common number(s): " + str(most_common).strip('[]'))
print("Times occured: " + str(max_count))


def change(aString):
    aString.upper()
    return aString


def main():
    myString = "hello"
    result = change(myString)
    print(result)


main()

clone = 5
while clone > 0:
    print("Make it double!")
    clone = clone - 1
