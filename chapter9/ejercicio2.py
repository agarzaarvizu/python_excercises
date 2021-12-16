filename = input("Ingresa un nombre de archivo: ")
days_dict = {}
counter_fri = 0
counter_thu = 0
counter_sat = 0

try:
    document = open(filename)
    for line in document:
        line = line.rstrip()
        if not line == "" and line.startswith("From") and not line.startswith("From:"):
            list_of_words = line.split(" ")
            if list_of_words[2] == "Fri":
                counter_fri = counter_fri + 1
                days_dict[list_of_words[2]] = counter_fri
            elif list_of_words[2] == "Thu":
                counter_thu = counter_thu + 1
                days_dict[list_of_words[2]] = counter_thu
            elif list_of_words[2] == "Sat":
                counter_sat = counter_sat + 1
                days_dict[list_of_words[2]] = counter_sat
    print(days_dict)
            
except:
    print("Nombre de archivo invalido: %s" % filename)
