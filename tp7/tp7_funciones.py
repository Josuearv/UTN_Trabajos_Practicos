#Funciones ejercicio 1

def numbers_bubble_sort(list):

    large_list = len(list)
    for i in range(large_list):
        for j in range(large_list-1):
            if list[j] > list[j+1]:
                var = list[j]
                list[j] = list[j+1]
                list[j+1] = var
    return list

#Funciones ejercicio 2

def caracter_selection_sort(list):
    large_list = len(list)
    for i in range(large_list):
        min_index = i
        for j in range(i, large_list):
            if (list[j][0]) < (list[min_index][0]): 
                var = list[j]
                list[j] = list[min_index]
                list[min_index] = var
    return list

#Funciones ejercicio 3

def sort_books_by_field(book, field):
    return sorted(book, key=lambda x: x[field])

#Funciones ejercicio 4

def large_string_insertion_sort(list):
    large_list = len(list)
    for i in range(large_list):
        min_index = i
        for j in range(i, large_list):
            if len(list[j]) < len(list[min_index]): 
                var = list[j]
                list[j] = list[min_index]
                list[min_index] = var
    return list


#Funciones ejercicio 5

def large_string_insertion_invested(list):
    large_list = len(list)
    for i in range(large_list):
        min_index = i
        for j in range(i, large_list):
            if len(list[j]) > len(list[min_index]): 
                var = list[j]
                list[j] = list[min_index]
                list[min_index] = var
    return list


#Funciones ejercicio 6

def sort_by_count(list):

    max_val = max(list)
    min_val = min(list)

    counter = [0] * (max_val - min_val + 1)

    for num in list:
        counter[num - min_val] += 1

    list_sort = []
    for i in range(len(counter)):
        list_sort.extend([i + min_val] * counter[i])

    return list_sort


#Funciones ejercicio 7

def items_list_sort(list):
    large_list = len(list)
    number_list = []
    string_list = []
    list_sort = []
    for i in range(large_list):
        if isinstance(list[i], str):
            string_list.append(list[i])
        elif isinstance(list[i], int):
            number_list.append(list[i])
    
    number_list = numbers_bubble_sort(number_list)

    string_list = caracter_selection_sort(string_list)

    list_sort = number_list + string_list
    return list_sort

#Funciones ejercicio 8

def merge_sort(list):
    if len(list) > 1:
        
        half = len(list) // 2
        half_left = list[:half]
        half_right = list[half:]

        merge_sort(half_left)
        merge_sort(half_right)

        i = j = k = 0

        while i < len(half_left) and j < len(half_right):
            if half_left[i] < half_right[j]:
                list[k] = half_left[i]
                i += 1
            else:
                list[k] = half_right[j]
                j += 1
            k += 1

        while i < len(half_left):
            list[k] = half_left[i]
            i += 1
            k += 1

        while j < len(half_right):
            list[k] = half_right[j]
            j += 1
            k += 1