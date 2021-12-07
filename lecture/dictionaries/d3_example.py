# reads the file frost.txt
# counts unique words
# counts how many times each word appears in the file

def main():
    filename = "frost.txt"
    infile = open(filename, "r")
    count = {}

    for line in infile:
        line = line.strip("\n")  # take away new line characters
        line = line.lower()  # make all lowercase
        for punctuation in ".,":
            # remove punctuation from line
            line = line.replace(punctuation, "")
        for word in line.split():  # line.split creates a list of words
            # count word occurrence in dictionary
            count[word] = count.get(word, 0) + 1
    infile.close()

    print("The number of unique words is: " + str(len(count)))
    print("The number of occurences for each word are: ")

    outfile = open("frost_results.txt", "w")
    for item in count.items():
        print(item[0] + " : " + str(item[1]))
        outfile.write(item[0] + " : " + str(item[1]) + "\n")
    outfile.close()


main()
