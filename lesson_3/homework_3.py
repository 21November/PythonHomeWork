# Task 1:
# Task 1.1:
list_1 = [1, 2, 3, 4, 5]
# Task 1.2:
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
# region comments for homework 3 tasks 1-3
# TODO: common issue - You should numerate each sub task with some comment
# TODO: common issue - You should wrap blocks of functional code into regions. It will allow you to expand and
#                      collapse it into lists.
# TODO: common issue - Hard to understand all this prints. Please add description for each print. For example "Not
#                      sorted list", "Sorted list"
# TODO: common issue - before next push try to sue code analyzer > Code -> Inspect Code -> Whole project -> OK.
#                      Remove all warnings issues and errors from iteration to iteration until no errors left.
# TODO: line 4 - make space after comma
# TODO: line 7 - customization of str to str make no sense
# TODO: line 9 - best practice to use one code style. In python no difference between such two strings 'Python' and
#                "Python". Try to use single quotes for internal strings or for separated characters ("my outer
#                string 'my inner string'", "Simple string", '\n', 'n').
# TODO: lines 16-17 - please write difference between both methods. Try to print result of this functions to see
#                     difference.
# TODO: line 19 - you print almost same lists as in task 1. Please create 1 set of variables for work but with noto
#                 so confusing names.
# TODO: line 21 - no space after # before comment text
# TODO: line 30 - 2 emtpy lines should be before function declaration.
# TODO: line 33 - all variables and attributes should be lower case with underscore
# TODO: line 36 - all variables and attributes should be lower case with underscore
# TODO: line 31 - why do you create another one internal variable of array if you can use array from arguments?
# TODO: line 31 - variable name is confusing and not clear destination of such variable
# TODO: line 32 - variable name is confusing and not clear destination of such variable
# TODO: line 34 - variable name is confusing and not clear destination of such variable
# TODO: line 37 - variable name is confusing and not clear destination of such variable
# TODO: lines 31 - 40 - no comments. Please add some comments about work of your algorithm.
# TODO: line 42 - no empty line after code
# endregion
