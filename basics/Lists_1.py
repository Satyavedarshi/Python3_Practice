import math, copy
from collections import Counter

def interchange_first_last(input_list):
    first, *remains, last = input_list
    return [last,*remains, first]

def swap_by_pos(input_list,pos1,pos2):
    input_list[pos1], input_list[pos2] = input_list[pos2], input_list[pos1]
    return input_list

def second_max(input_list):
    new_list = list(set(input_list))
    return new_list[-2]

def n_maxelems(input_list,num):
    return list(set(input_list))[-num:]

def by_even(input_list):
    return list(filter(lambda x: (x%2==0),input_list)), list(filter(lambda x: (x%2!=0),input_list))

def removeall_list(input_list,item):
    for i in input_list:
        if i == item:
            input_list.remove(i)
    return input_list

def rem_empty_lists(input_list):
    return list(filter(None,input_list))

def counter_list(input_list):
    return Counter(input_list)

def ret_duplicates(input_list):
    counts = Counter(input_list)
    return list(i for i in counts if counts[i] > 1)

def cum_sum(input_list):
    cum_list = []
    cum_list.append(input_list[0])
    for i in range(1,len(input_list)):
        cum_list.append(cum_list[i-1] + input_list[i])
    return cum_list

def div_list_n(input_list,n):
    return [L1[i:i+n] for i in range(0,len(input_list),n)]


L1 = [1,2,3,4,5,6,1,2,3]
print(L1)
print(interchange_first_last(L1))

print(swap_by_pos(L1,0,3))

print(L1[::-1])
print([i for i in reversed(L1)])
print(L1)
print(math.prod(L1))
print(L1)
print(second_max(L1))

print('Two Large elements in the list are - ',n_maxelems(L1,2))

print('Even numbers and odd numbers in list are - ', by_even(L1))

print(L1)
print(removeall_list(L1,2))

L1.append([])
L1.append([])
L1[2] = []
L1.append([])
L1.append([])

print(L1)

L1 = copy.deepcopy(rem_empty_lists(L1))
print(L1)
print('Counter')
print(counter_list(L1))

L1.append(4)

print(ret_duplicates(L1))

print(cum_sum(L1))

print(div_list_n(L1,3))

