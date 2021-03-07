import re, string, random
from collections import Counter, OrderedDict
from itertools import permutations

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
def rep_dup_1(test_str):
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

def rep_dup_2(test_str):
    replace_strings = {'Gfg': 'It', 'Classes': 'They'}
    str_list = test_str.split()
    res = set()
    for i in enumerate(str_list):
        print(i)
        if i[1] in replace_strings:
            if i[1] not in res:
                res.add(i[1])
            else:
                str_list[i[0]] = replace_strings[i[1]]
    return ' '.join(str_list)

def rep_dup_3(test_str):
    word_list = ["best", 'CS', 'for']
    for i in word_list:
        if i in test_str:
            test_str = re.sub(i,'gfg',test_str)
    return test_str

#Python | Permutation of a given string using inbuilt function
def perm_str(test_str):
    print(*[''.join(i) for i in permutations(test_str)],sep='\n')


#Check for URL in a String
def check_url(test_str):
    urls = re.findall(re.compile(url_regex),test_str)
    print(urls)

#Execute a String of Code in Python
def exec_str(test_str):
    exec(test_str)

#String slicing in Python to check if a string can become empty by recursive deletion
def rec_del(test_str,del_str):
    while(len(test_str)>0):
        index1 = test_str.find(del_str)
        if index1 != -1:
            test_str = test_str[0:index1] + test_str[index1+len(del_str):]
        else:
            return False
    return True

#Replace all occurrences of a substring in a string
def replac_all(test_str,sub_str,rep_str):
    replace_str = str.maketrans(sub_str,rep_str)
    test_str = test_str.translate(replace_str)
    return test_str

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


print(rep_dup_1('Gfg is best . Gfg also has Classes now. Classes help understand better . '))
print(rep_dup_2('Gfg is best . Gfg also has Classes now. Classes help understand better . '))
print(rep_dup_3('Geeksforgeeks is best for geeks and CS'))

print(perm_str('ABC'))

#print(check_url('My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles \
#in the portal of http://www.geeksforgeeks.org/'))


exec_str('a=6+5\nprint("the sum is ",a)')

print(rec_del('GEEGEEKSKS','GEEKS'))
print(rec_del('GEEGEEKSKES','GEEKS'))

print(replac_all('geeksforgeeks','geek','abcd'))
