filename = input("Ingresa un nombre de archivo: ")
time_list = list()
hours_list = list()
unique_hours = list()
counter = dict()
t = list()

try:
    document = open(filename)
    
    # Create the list of all hours in the document
    for line in document:
        line = line.rstrip()
        if not line == "" and line.startswith("From") and not line.startswith("From:"):
            line_list = line.split(" ")
            time_list.append(str(line_list[6]))

    # Create a list with just the hour
    for time in time_list:
        time_splited = time.split(":")
        hours_list.append(time_splited[0])

    # Create a list with unique hours
    for hour in hours_list:
        if not hour in unique_hours:
            unique_hours.append(hour)

    # Create a dictionary
    for hour in unique_hours:
        value = hours_list.count(hour)
        counter[hour] = value

    # Create a list of tuples
    for hour, count in counter.items():
        t.append((hour, count))

    # Sort tuples
    t.sort()

    # Print tuples
    for hour, value in t:
        print(hour, value)


except Exception as Error:
    print(Error)
    print("Nombre archivo invalido: %s" % filename)
