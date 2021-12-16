filename = input("Ingresa un nombre de archivo: ")
list_of_mails = []
list_of_words = []
mails_dict = {}

try:
    document = open(filename)
    for line in document:
        line = line.rstrip()
        if not line == "" and line.startswith("From")  and not line.startswith("From:"):
            list_line = line.split(" ")
            list_of_words.append(list_line[1])
            if not list_line[1] in list_of_mails:
                list_of_mails.append(list_line[1])
    for mail in list_of_mails:
        number = list_of_words.count(mail)
        mails_dict[mail] = number
    print(mails_dict)

except:
    print("Nombre de archivo invalido: %s" % filename)
