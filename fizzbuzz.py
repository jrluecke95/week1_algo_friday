num = int(input("what number would you like to choose? "))
num_list = []
for num in range(num + 1):
    if num == 0:
        None
    if num % 3 == 0 and num % 5 != 0:
        num_list.append("fizz")
    elif num % 5 == 0 and num % 3 != 0:
        num_list.append("buzz")
    elif num % 3 == 0 and num % 5 == 0:
        num_list.append("fizzbuzz")
    else:
        num_list.append(num)
print(num_list)