filename = input("Ingresa un nombre de archivo: ")
list_of_mails = []
list_of_words = []
mails_dict = {}
mayor = None

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
    values = mails_dict.values()
    max_value = max(values)
    for key, value in mails_dict.items():
        if mayor is None or value > mayor:
            mayor = value
            mayor_name = key
    print(mayor_name, mayor)


except Exception as Error:
    print(Error)
    #print("Nombre de archivo invalido: %s" % filename)
