import numpy
from itertools import zip_longest

#Python program to add two Matrices
def add_matrices_1(list1,list2):
    sum_list = []
    for rows in range(len(list1)):
        sum_list.append([])
        print(sum_list)
        for cols in range(len(list1[rows])):
            sum_list[rows].append([])
            print(sum_list)
            sum_list[rows][cols] = list1[rows][cols] + list2[rows][cols]
    return sum_list

def add_matrices_2(list1,list2):
    print(*[lists for lists in zip(list1,list2)],sep='\n')
    return [list(map(sum,zip(*lists))) for lists in zip(list1, list2)]

def mul_matrices(list1,list2):
    return numpy.dot(list1,list2)

def prod_matrix(input_list):
    prod_output = 1
    for i in input_list:
        if type(i) != int :
            prod_output *= prod_matrix(i)
        else:
            prod_output *= i
    return prod_output

def get_size_matrix(input_list):
    rows = len(input_list)
    cols = len(input_list[0])
    return rows,cols

def transpose_mat(input_list):
    rows,cols = get_size_matrix(input_list)
    for i in range(0,rows):
        for j in range(i,cols):
            if i != j:
                temp = input_list[i][j]
                input_list[i][j] = input_list[j][i]
                input_list[j][i] = temp
    return input_list

def create_mat(dim):
    insert_elem = 0
    L = []
    for i in range(0,dim):
        L.append([])
        for j in range(0,dim):
            L[i].append(insert_elem + j+1)
        insert_elem = L[i][dim-1]
    return L

def get_k_column(k,input_list):
    return list(row[k-1] for row in input_list)

#Python – Vertical Concatenation in Matrix
def vert_concat(input_list):
    return [''.join(item) for item in zip_longest(*input_list,fillvalue='nope')]

print('Sum of two matrices is ', add_matrices_1([[1,2,3],[4 ,5,6],[7 ,8,9]],   [[9,8,7],[6,5,4],[3,2,1]]))

print('Sum of two matrices is ', add_matrices_2([[1,2,3],[4 ,5,6],[7 ,8,9]],   [[9,8,7],[6,5,4],[3,2,1]]))

print('Multiplication of matrices is : ', mul_matrices([[12, 7, 3], [4, 5, 6], [7, 8, 9]] , [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]))


print(prod_matrix([[1,2,3,[4,4,5]],[4 ,5,6],[7 ,8,9]]))

print(get_size_matrix([[1,2,3,],[4 ,5,6],[7 ,8,9]]))

print(transpose_mat([[1,2,3],[4 ,5,6],[7 ,8,9]]))

print(create_mat(3))

print('Kth column of the matrix is ', get_k_column(3,[[1,2,3],[4,5,6],[7 ,8,9]]))


print('Column concatinated Matrix is ', vert_concat([['Gfg', 'good', 'geeks'], ['is', 'for', 'best']]))
