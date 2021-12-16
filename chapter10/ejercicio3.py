import string

filename = input("Ingresa el nombre de un archivo: ")
all_letters = list()
unique_letters = list()
counter = dict()
t = list()

try:
    document = open(filename)

    #Cleaning each line
    for line in document:
        line = line.rstrip()
        line = line.translate(line.maketrans("","", string.punctuation))
        line = line.translate(line.maketrans("","", string.digits))
        line = line.lower()
        words = line.split()

        # Checking each line and adding each letter
        for word in words:
            for letter in word:
                all_letters.append(letter)
                if not letter in unique_letters:
                    unique_letters.append(letter)

    # Counting each letter and adding to the dictionary
    for letter in unique_letters:
        value = all_letters.count(letter)
        counter[letter] = value

    # Creating a list of tuples
    for letter, value in counter.items():
        t.append((value,letter))

    # Sorting the list and printing
    t.sort(reverse = True)
    for value, letter in t:
        print(letter, value)


except Exception as Error:
    print(Error)
    print("Nombre de archivo invalido")
