import itertools
from operator import itemgetter
from collections import OrderedDict


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
