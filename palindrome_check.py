string = input("what word would you like me to check? ").lower()

string_list = []
for letter in string:
    string_list.append(letter)

reverse_list = []
counter = -1
for i in range(len(string)):
    reverse_list.append(string[counter])
    counter -= 1

reverse_string = "".join(reverse_list)
if reverse_string == string:
    print('this is a palindrome!')
else:
    print("this is not a palindrome")