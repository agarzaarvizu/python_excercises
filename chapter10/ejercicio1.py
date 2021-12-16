filename = input("Ingresa un nombre de archivo: ")
mails_list = list()
unique_mails = list()
counter = dict()
t = list()

try:
    document = open(filename)
    
    # Create the list of all mails in the document
    for line in document:
        line = line.rstrip()
        if not line == "" and line.startswith("From") and not line.startswith("From:"):
            line_list = line.split(" ")
            mails_list.append(line_list[1])

    # Create a list with unique mails
    for mail in mails_list:
        if not mail in unique_mails:
            unique_mails.append(mail)

    # Create dictionary for mails and number
    for mail in unique_mails:
        number = mails_list.count(mail)
        counter[mail] = number

    # Create list of tuples
    for mail, count in counter.items():
        t.append((count,mail))

    # Sort list and print the most repeated mail
    t.sort(reverse = True)
    count, mail = t[0]
    print(mail, count)


except:
    print("Nombre de archivo invalido: %s" % filename)
