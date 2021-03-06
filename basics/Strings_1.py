import re, string, random
from collections import Counter, OrderedDict

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

#Python program to check whether the string is Symmetrical
def check_symm(test_str):
    if test_str[:len(test_str)//2] != test_str[len(test_str)//2:]:
        return False
    return True

#Reverse words in a given String in Python
def rev_words(test_str):
    return ' '.join(test_str.split(' ')[::-1])

#Check if a Substring is Present in a Given String
def check_substr_1(substr,test_str):
    if test_str.find(substr) == 0:
        return test_str.count(substr)
    return False

def check_substr_2(substr,test_str):
    if re.search(substr,test_str):
        return re.findall(substr,test_str)
    return False

#Python – Words Frequency in String Shorthands
def count_str(test_str):
    return dict(Counter(test_str.split())),{i:test_str.count(i) for i in test_str.split()}

#Convert Snake case to Pascal case
def conv_str(test_str):
    return test_str.title().replace('_',''),string.capwords(test_str).replace('_',''), test_str.split('_'), test_str.count('gee')

# Program to accept the strings which contains all vowels
def check_vowels(test_str):
    vows_lows = ['a','e','i','o','u']
    if all(True if i in test_str or i.capitalize() in test_str else False for i in vows_lows ):
        return 'All vowels are present'
    return 'Not allowed'

#Count the Number of matching characters in a pair of string
def count_matches(str1,str2):
    return len(set(str1).intersection(set(str2)))

#Remove all duplicates from a given string in Python
def rem_dups(test_str):
    return ''.join(OrderedDict.fromkeys(test_str))
    #return ''.join(sorted(set(test_str)))

#Python – Least Frequent Character in String
def least_freq(test_str):
    return sorted(Counter(test_str).items(),key = lambda tup : tup[1])[0][0]

#Program to check if a string contains any special character
def check_specials(test_str):
    expected_string = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' '
    if all([True if i in expected_string else False for i in test_str]):
        return 'String is accepted'
    return 'String is NOT accepted'

#Generating random strings until a given string is generated
def gen_ran_str(test_str):
    loop_count = 1
    while(loop_count):
        rand_str = ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(0,len(test_str))])
        print(rand_str)
        if test_str == rand_str:
            print('Found in iteration - ', loop_count)
            return rand_str
        loop_count += 1

#Python | Check if a given string is binary string or not
def check_bin(test_str):
    bin_vals = '01'
    if all([True if i in bin_vals else False for i in test_str]):
        return True
    return False

#Python program to find uncommon words from two Strings
def uncommon_strings(str1,str2):
    return set(str1.split()).symmetric_difference(set(str2.split()))

#Python – Replace duplicate Occurrence in String
def rep_dup(test_str):
    replace_strings = {'Gfg' :  'It', 'Classes' : 'They' }
    str_list = test_str.split()
    for items in replace_strings.items():
        print(items)
        if items[0] in str_list and Counter(str_list)[items[0]] > 1:
            counter = 0
            print(str_list)
            for i in range(0,len(str_list)):
                if items[0] == str_list[i] and counter==0 :
                    counter += 1
                elif items[0] == str_list[i] and counter>0 :
                    str_list[i] = items[1]
    print(' '.join(str_list))



print(check_pallind_1('malayalam'), check_pallind_1('malayala'))

print(check_pallind_2('malayalam'), check_pallind_2('malayala'))

print(check_symm('khokho'), check_symm('malayala'))

print(rev_words('geeks quiz practice code'))

print(check_substr_1('geeks','geeks for geeks'))

print(check_substr_2('geeks','geeks for geeks'))

print(count_str('geeks for geeks is for the new geek'),sep='\n')

print(conv_str('geeksforgeeks_is_best'))

print(check_vowels('ABeeIhiObhkUul'), check_vowels('geeksforgeeks'))

print(count_matches('aabcddekll12@','bb22ll@55k'))

print(rem_dups('geeksforgeeks'))

print(least_freq('geeksforgeeks'))


print(check_specials('geeks for geeks'))

#print(gen_ran_str('FyFJ'))

print(check_bin('0001010'))

print(uncommon_strings('Geeks for Geeks','Learning from Geeks for Geeks'))


print(rep_dup('Gfg is best . Gfg also has Classes now. Classes help understand better . '))

