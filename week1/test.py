num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
enum_list = enumerate(num_list)
count = 0


for i in enum_list:
    count += 1
    if i[1] == 36:
        print("Number found at position: " + str(i[0]))
        break

print(count)