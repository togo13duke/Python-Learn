import re

file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "regex_sum_42.txt"

try:
    handle = open(file_name)
except:
    print("Invalid file name")

num_list = list()

for line in handle:
    line = line.rstrip()
    if re.search("[0-9]+", line) is None :continue
    temp_list = re.findall("[0-9]+",line)

    for str_num in temp_list:
        num_list.append(int(str_num))


print(sum(num_list))