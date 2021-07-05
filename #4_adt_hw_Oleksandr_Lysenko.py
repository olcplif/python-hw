from functools import reduce

# 1. Define the id of next variables:
int_a = 55
print("#1.", f'Id int_a = {id(int_a)}')  # OUTPUT: Id int_a = 9790336

str_b = 'cursor'
print(f'Id str_b = {id(str_b)}')  # OUTPUT: Id str_b = 139747073096944

set_c = {1, 2, 3}
print(f'Id set_c = {id(set_c)}')  # OUTPUT: Id set_c = 139747073063840

lst_d = [1, 2, 3]
print(f'Id lst_d  = {id(lst_d)}')  # OUTPUT: Id lst_d  = 139747073140416

dict_e = {'a': 1, 'b': 2, 'c': 3}
print(f'Id dict_e = {id(dict_e)}')  # OUTPUT: Id dict_e = 139747073921600

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print("#2.", f'Id lst_d = {id(lst_d)} ==> The ID differs after each new start of the program')
# OUTPUT: Id lst_d = 139747073140416 ==> The ID differs after each new start of the program

# 3. Define the type of each object from step 1.
print(f'#3. Type int_a = {type(int_a)}')  # OUTPUT: Type int_a = <class 'int'>
print(f'Type str_b = {type(str_b)}')  # OUTPUT: Type str_b = <class 'str'>
print(f'Type set_c = {type(set_c)}')  # OUTPUT: Type set_c = <class 'set'>
print(f'Type lst_d  = {type(lst_d)}')  # OUTPUT: Type lst_d  = <class 'list'>
print(f'Type dict_e = {type(dict_e)}')  # OUTPUT: Type dict_e = <class 'dict'>


# 4*. Check the type of the objects by using isinstance.
def type_definition(obj):
    answer = ''
    if isinstance(obj, str):
        answer = "this str type"
    elif isinstance(obj, int):
        answer = "this int type"
    elif isinstance(obj, list):
        answer = "this list type"
    elif isinstance(obj, dict):
        answer = "this dict type"
    elif isinstance(obj, set):
        answer = "this set type"
    elif isinstance(obj, tuple):
        answer = "this tuple type"
    elif isinstance(obj, float):
        answer = 'this float type'
    return answer


def name_var(**variables):
    return [v for v in variables]


print("#4.", name_var(int_a=int_a), type_definition(int_a))  # OUTPUT: #4. ['int_a'] this int type
print(name_var(str_b=str_b), type_definition(str_b))  # OUTPUT: ['str_b'] this str type
print(name_var(set_c=set_c), type_definition(set_c))  # OUTPUT: ['set_c'] this set type
print(name_var(lst_d=lst_d), type_definition(lst_d))  # OUTPUT: ['lst_d'] this list type
print(name_var(dict_e=dict_e), type_definition(dict_e))  # OUTPUT: ['dict_e'] this dict type

# 5. With .format and curly braces {}
print('#5. Anna has {} apples and {} peaches.'.format("5", "five"))
# OUTPUT: #5. Anna has 5 apples and five peaches.

# 6. By passing index numbers into the curly braces.
print('#6. Anna has {1} apples and {0} peaches.'.format("six", "6"))
# OUTPUT: #6. Anna has 6 apples and six peaches.

# 7. By using keyword arguments into the curly braces.
print('#7. Anna has {apple} apples and {peach} peaches.'.format(apple="seven", peach="7"))
# OUTPUT: #7. Anna has seven apples and 7 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('#8. Anna has {0:5} apples and {1:3} peaches.'.format("8", "eight"))
# OUTPUT: #8. Anna has 8     apples and eight peaches.

# 9. With f-strings and variables
apple, peach = 9, 99
print(f'#9. Anna has {apple} apples and {peach} peaches.')
# OUTPUT: #9. Anna has 9 apples and 99 peaches.

# 10. With % operator
apple, peach = 10, 110
print(f'#10. Anna has %s apples and %s peaches.' % (apple, peach))
# OUTPUT: #10. Anna has 10 apples and 110 peaches.

# 11*. With variable substitutions by name (hint: by using dict)
dct_fruits = {apple: 11, peach: 111}
print(f'#11. Anna has {dct_fruits[apple]} apples and {dct_fruits[peach]} peaches.')
# OUTPUT: #11. Anna has 11 apples and 111 peaches.

# 12. Convert (1) to list comprehension

lst_to_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print("#12.", lst_to_comprehension)
# OUTPUT: #12. [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else
list_from_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_from_comprehension.append(num // 2)
    else:
        list_from_comprehension.append(num * 10)
print("#13.", list_from_comprehension)
# OUTPUT: #13. [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14. Convert (3) to dict comprehension.
d1_to_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print("#14.", d1_to_comprehension)
# OUTPUT: #14. {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.
d2_to_comprehension = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print("#15.", d2_to_comprehension)
# OUTPUT: #15. {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
dict5_from_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict5_from_comprehension[x] = x ** 3
print("#16.", dict5_from_comprehension)
# OUTPUT: #16. {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.
dict6_from_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict6_from_comprehension[x] = x ** 3
    else:
        dict6_from_comprehension[x] = x
print("#17.", dict6_from_comprehension)
# OUTPUT: #17. {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# 18. Convert (7) to lambda function
foo_1 = lambda x, y: x if x < y else y
print("#18.", foo_1(3, 7))  # OUTPUT: #18. 3


# 19*. Convert (8) to regular function
def foo_2(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print("#19.", foo_2(1, 6, 3))  # OUTPUT: #19. 6

# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print("#20.", sorted(lst_to_sort))
# OUTPUT: #20. [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min
print("#21.", sorted(lst_to_sort, reverse=True))
# OUTPUT: #21. [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
multi_list = list(map(lambda x: x * 2, lst_to_sort))
print("#22.", multi_list)
# OUTPUT: #22. [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]


def raise_list(list_1, list_2):
    list_res = []
    for i in range(len(list_1)):
        list_res.append(list_1[i] ** list_2[i])
    return list_res


print("#23.", raise_list(list_A, list_B))  # OUTPUT: #23. [32, 729, 16384]
# Without def:
new_raise_list = list(map(lambda x, y: x ** y, list_A, list_B))
print("#23_1.", new_raise_list)  # OUTPUT: #23_1. [32, 729, 16384]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

list_compute = reduce((lambda i, j: i + j), lst_to_sort)
print("#24.", list_compute)  # OUTPUT: #24. 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
new_list_filter = list(filter(lambda elem: (elem % 2 == 1), lst_to_sort))
print("#25.", new_list_filter)
# OUTPUT: #25. [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

new_list_filter_from_range = list(filter(lambda elem: (elem < 0), range(-10, 10)))
print("#26.", new_list_filter_from_range)
# OUTPUT: #26. [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
new_list_filter_are_common = list(filter(lambda item_1: (item_1 in list_2), list_1))
print("#27.", new_list_filter_are_common)
# OUTPUT: #27. [2, 3, 5, 7]
