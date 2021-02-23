from collections import Counter
from functools import reduce
from random import shuffle

def sort_by_newlist(l1,l2):
    zipped_list = dict(zip(l1,l2))
    print(zipped_list)
    return [i[0] for i in sorted(zipped_list.items(),key=lambda value:value[1])]

def ret_str_k(input_list,key):
    return [i[0] for i in Counter(input_list).items() if i[1] == key]

def list_to_sets(input_list):
    for index in range(0,len(input_list)):
        input_list[index] = set(input_list[index])
    index = 0
    while(index < len(input_list)):
        in_index = index + 1
        for each_set in input_list[index+1:]:
            if any(True for i in input_list[index] if i in each_set):
                input_list[index] = input_list[index].union(input_list.pop(in_index))
            in_index += 1
        else:
            index += 1
    return input_list

def prod_consec_nums(input_list,k):
    len_list = len(input_list)
    key = k
    for i in range(0,len_list-k+2):
        if k <= len_list:
            input_list[i] = reduce(lambda x,y : x*y, input_list[i:k])
            k+=1
        else:
            return input_list[0:i]

def rate_redundancy(input_list):
    for i in range(0,len(input_list)):
        counts = Counter(input_list[i])
        input_list[i] = 1 - len(counts)/len(input_list[i])
    return input_list

#Python Program to find the Next Nearest element in a Matrix
def next_near(input_list,i,j,num):
    start = 0
    for rows in range(i,len(input_list)):
        if start ==0:
            cols = j+1
            start += 1
        else:
            cols = 0
        while (cols < len(input_list[rows])):
            cols+=1
            if num == input_list[rows][cols]:
                return (rows,cols)

#Python – Total equal pairs in List
def eq_pairs(input_list):
    counts = Counter(input_list)
    return len([i for i in counts.values() if i>1])

#Python program to randomly create N Lists of K size
def gen_nlists(input_list,key,nums):
    res_list = []
    for i in range(0,nums):
        shuffle(input_list)
        res_list.append(input_list[:key])
    return res_list

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]


print(sorted(list1))

print(sort_by_newlist(list1,list2))

str1 = 'banana is in yellow and sun flower is also in yellow'
print(ret_str_k(str1.split(),2))

L1 = [[15, 14, 12, 18], [9, 5, 2, 1], [4, 3, 2, 1], [19, 11, 13, 22]]

print(list_to_sets(L1))

print(prod_consec_nums([5, 6, 2, 1, 7, 5, 3],4))

print(rate_redundancy([[4, 5, 2, 4, 3], [5, 5, 5, 5, 5], [8, 7, 8, 8, 7], [1, 2, 3, 4, 5]]))

print(next_near([[4, 3, 1, 2, 3], [7, 5, 3, 6, 3], [8, 5, 3, 5, 3], [1, 2, 3, 4, 6]],2,4,3))

print(eq_pairs([2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3, 3]))

print(gen_nlists([6, 9, 1, 8, 4, 7],3,4))

