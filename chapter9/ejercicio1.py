document = open("../files/words.txt")
dict_of_words = {}
counter = 0

for line in document:
    line = line.rstrip()
    list_of_words = line.split(" ")
    if not len(list_of_words) == 0:
        for word in list_of_words:
            dict_of_words[word] = counter
            counter = counter + 1

print(dict_of_words)

