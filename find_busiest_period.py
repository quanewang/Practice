def find_busiest_period(data):
    busiest = 0
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
                           [1487800378, 10, 1],
                           [1487801478, 18, 0],
                           [1487801478, 18, 1],
                           [1487901013, 1, 0],
                           [1487901211, 7, 1],
                           [1487901211, 7, 0]]))
