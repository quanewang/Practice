def find_busiest_period(data):
    busiest = data[0][0]
    i = 0
    current = data[0][0]
    counter = 0
    maxPointer = 0
    for i in range(len(data)):
        if data[i][0] == current:
            counter = update_counter(data[i], counter)
        else:
            if maxPointer < counter:
                maxPointer = counter
                busiest = current
            current = data[i][0]
            counter = update_counter(data[i], counter)

    if maxPointer < counter:
        busiest = current
    
    return busiest


def update_counter(data, counter):
    if data[2] == 1:
        counter += data[1]
    else:
        counter -= data[1]
    return counter


print(find_busiest_period([[1487799425, 14, 1],
                           [1487799425, 4, 0],
                           [1487799425, 2, 0],
                           [1487800378, 10, 1]]))
