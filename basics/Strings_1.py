
#Python program to check if a string is palindrome or not
#Using Loops
def check_pallind_1(test_str):
    str_len_index = len(test_str) - 1
    print(str_len_index)
    for i in range(0,str_len_index+1):
        if test_str[i] != test_str[str_len_index-i]:
            return False
    else:
        return True
#Python program to check if a string is palindrome or not
#Using Reversed
def check_pallind_2(test_str):
    if test_str != ''.join(reversed(test_str)):
        return False
    return True



print(check_pallind_1('malayalam'), check_pallind_1('malayala'))

print(check_pallind_2('malayalam'), check_pallind_2('malayala'))