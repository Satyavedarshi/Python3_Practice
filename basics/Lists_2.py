

def sort_by_newlist(l1,l2):
    zipped_list = dict(zip(l1,l2))
    print(zipped_list)
    return [i[0] for i in sorted(zipped_list.items(),key=lambda value:value[1])]






list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]


print(sorted(list1))

print(sort_by_newlist(list1,list2))