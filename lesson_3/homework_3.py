# Task 1:

list_1 = [1, 2, 3, 4, 5]
list_2 = [x**2 for x in [1,2,3,4]]
text_1 = "Python"
list_3 = list(text_1)
list_4 = [str(x) for x in text_1]

print('Task 1:', list_1, list_2, list_3, list_4, sep='\n')

# Task 2:

list_1.append(6)         # Add item to the end of the list_1
list_2.insert(1, 10)     # Add item to list_2 at fixed index
del list_3[-1]           # Remove item from list_3 at fixed index
list_1.remove(3)         # The function removes a specific list_1 item.
list_2.pop(0)            # The function 'pop' deletes a list item by its index

print('Task 2:', list_1, list_2, list_3[-1], list_1[3], list_3, list_1, list_2, sep='\n')

#Task 3:

list_5 = [21, 10, 18, 5, 15, 4, 2, 1, 30]
list_5.sort()                                 # sorting by increment list using function 'sort'
list_6 = [21, 10, 18, 5, 15, 4, 2, 1, 30]
list_6.reverse()                              # sorting the list in descending order using the function 'reverse'

print('Task 3:', list_5, list_6, sep='\n')

def selection_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        idxMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a

print(selection_sort(list_5))