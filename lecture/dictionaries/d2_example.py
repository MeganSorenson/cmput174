# counts the number of unique words that the user enters
# counts how many times a word appears in the input string entered by the user

def main():
    sentence = input("Enter a sentence >")
    sentence = sentence.lower()

    count = {}

    alist = sentence.split()  # split string at spaces that separate the words

    # count occurrences of each word
    for word in alist:
        count[word] = count.get(word, 0) + 1
        # if word not in count:
        # add
        #count[word] = 1
        # else:
        # update
        #count[word] += 1

    print("The number of unique words are: " + str(len(count)))
    print(count)


main()
