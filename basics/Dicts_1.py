import itertools
from operator import itemgetter
from collections import OrderedDict,Counter,defaultdict


# Extract Unique values dictionary values
def dup_vals(test_dict):
    return set(itertools.chain(*test_dict.values()))
    # return set(sorted([ele for vals in test_dict.values() for ele in vals]))


# Ways to sort list of dictionaries by values in Python – Using itemgetter
def sort_by_val(test_dict, test_key):
    return sorted(test_dict, key=lambda i: i[test_key])
    # return sorted(test_dict, key = itemgetter(test_key))


# Merging two Dictionaries
def merge_dicts(dict1, dict2):
    print({**dict1, **dict2})
    # dict1.update(dict2)


# Convert key-values list to flat dictionary
def flat_dict(test_dict):
    print(dict(zip(test_dict['month'],test_dict['name'])))

# Insertion at the beginning in OrderedDict
def inser_orddict(test_dict):
    print(dict5)
    dict5.update({'name1': 'name value1'})
    dict5.update({'name2': 'name value2'})
    dict5.update({'name3': 'name value3'})
    print(dict5)
    dict5.move_to_end('name3', last=False)
    print(dict5)
    dict5.move_to_end('name1')
    print(dict5)

# Check order of character in string using OrderedDict( )
def str_order(test_string,test_pat):
    temp_dict = OrderedDict.fromkeys(test_string,'Test')
    print(temp_dict)
    pat_ind = 0
    for keys in temp_dict.keys():
        if keys == test_pat[pat_ind]:
            pat_ind += 1
        if pat_ind == len(test_pat):
            return True
    return False

# Dictionary and counter in Python to find winner of election
def win_elec(test_list):
    counts = sorted(Counter(test_list).items(),key= lambda i : i[1])
    for i in counts:
        if i[1] == counts[-1][-1]:
            return i[0]

# Append Dictionary Keys and Values ( In order ) in dictionary
def app_dict(test_dict):
    return list(itertools.chain(test_dict.keys(),test_dict.values()))

# Sort Python Dictionaries by Key or Value
def sort_dict_key(test_dict):
    return [i[1] for i in sorted(test_dict.items(), key = lambda x : x[1])]

# Print anagrams together in Python using List and Dictionary
def list_anagrams(test_list):
    test_dict = {}
    for i in test_list:
        keys = ''.join(sorted(i))
        if keys in test_dict:
            test_dict[keys].append(i)
        else:
            test_dict[keys] = []
            test_dict[keys].append(i)
    return [j for i in test_dict.values() for j in i]

# K’th Non-repeating Character in Python using List Comprehension and OrderedDict
def k_nonrepeat(test_dict,keys):
    return list(dict(filter(lambda x : x[1] == 1,dict(Counter(test_dict)).items())).keys()).get[keys-1]

dict1 = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
dict2 = lis = [{"name": "Nandini", "age": 20}, {"name": "Manjeet", "age": 20}, {"name": "Nikhil", "age": 19}]
dict3 = {"name": "Nandini", "age": 20}
dict4 = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
dict5 = OrderedDict()

print(dup_vals(dict1))

print(dict1.pop('satya', 'No Key Found'))

print(sort_by_val(dict2, 'age'))

merge_dicts(dict1, dict3)

flat_dict(dict4)

inser_orddict(dict5)

print(str_order('engineers rock','er'), str_order('engineers rock','gsr'))

votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john","johnny", "jamie", "johnny", "john"]

print(win_elec(votes))

print(app_dict({'Gfg' : 1, 'is' : 2, 'Best' : 3}))

key_value = defaultdict(lambda : 'Key Not Found')
key_value[2] = '64'
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'

print(sort_dict_key(key_value))

print(key_value.setdefault(10,'Not'))
print(key_value.setdefault(10))

print(key_value[14])

print(list_anagrams(['cat', 'dog', 'tac', 'god', 'act']))

print(k_nonrepeat('geeksforgeeks',3))
