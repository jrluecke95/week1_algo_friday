num = int(input("What number would you like to choose? "))
num_list = []

for number in range(num + 1):
    num_list.append(number)

fib_list = []
iterables = range(0, len(num_list))

for i in iterables:
    if num_list[i] == 0:
        fib_list.append(num_list[i])
    elif num_list[i] == 1:
        fib_list.append(num_list[i])
    else:
        to_add = 0
        to_add = fib_list[i - 1] + fib_list[i - 2]
        if to_add >= num:
            break
        fib_list.append(to_add)


print(fib_list)


