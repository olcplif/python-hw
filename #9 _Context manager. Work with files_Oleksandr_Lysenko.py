dct = {}
keys_list = []
value_list = []

with open("files_contextmanagers/task1.txt", "r") as file:
    context_list = list(file.readlines())

# 1.1. Make Dict
for i in range(0, len(context_list), 2):
    keys_list.append(context_list[i])

for i in range(1, len(context_list), 2):
    value_list.append(context_list[i])

dct = dict.fromkeys(keys_list)

i = 0
for key in dct:
    dct.update({key: value_list[i]})
    i += 1

print(dct)

# 1.2. Make file

new_context_list = []

for i in range(1, len(context_list), 2):
    new_context_list.append(context_list[i].replace("\n", ""))

lst_to_str = ' '.join([str(elem) for elem in new_context_list])
print(lst_to_str)

with open("files_contextmanagers/task1-2.txt", "w") as file:
    file.write(lst_to_str)

# 2.1 List
