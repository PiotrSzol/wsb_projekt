def next_number(array):
    temp_array = sorted(array)
    length = len(temp_array)
    number = 0
    if length != 0:
        for i in range(1, length +1):
            if i not in temp_array:
                number = i
                break
            if i == length:
                number = i + 1
    else:
        number = 1
    return number


def array_of_number(instance):
    temp_array = []
    for row in instance.query.all():
        temp_array.append(row.numer)
    return temp_array

