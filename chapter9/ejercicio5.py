filename = input("Ingresa un nombre de archivo: ")
list_of_domains = []
list_of_words = []
domain_dict = {}
mayor = None
unique_domain = []

try:
    document = open(filename)
    for line in document:
        line = line.rstrip()
        if not line == "" and line.startswith("From")  and not line.startswith("From:"):
            list_line = line.split(" ")
            list_of_words.append(list_line[1])

    for mails in list_of_words:
        mail_list = mails.split("@")
        list_of_domains.append(mail_list[1])
        if not mail_list[1] in unique_domain:
            unique_domain.append(mail_list[1])
            
    for domain in unique_domain:
        number = list_of_domains.count(domain)
        domain_dict[domain] = number

    print(domain_dict)

except:
    print("Nombre de archivo invalido: %s" % filename)
