
import array,functools

def sum_array_1(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def max_min_arr(arr):
    max_var = arr[0]
    min_var = arr[0]
    for i in arr:
        if max_var < i:
            max_var = i
        if min_var > i:
            min_var = i
    return max_var,min_var

def rotate_arr_1(arr,rot_by):
    return arr[rot_by:len(arr)+1] + arr[0:rot_by]

def arr_mul_div(arr,div_by):
    return functools.reduce(lambda x,y : x*y, arr)%div_by

def check_arr_monotonic(arr):
    print(arr)
    return (all(True if arr[i] <= arr[i+1] else False for i in range(0,len(arr)-1))) or (all(True if arr[i] >= arr[i+1] else False for i in range(0,len(arr)-1)))

arr1 = array.array('i',{4,5,6,1,2,3})
print(arr1)
print(sum_array_1(arr1))

print('Max , Min values in array',max_min_arr(arr1))

print('Rotated list is - ',rotate_arr_1(arr1,1))

print('Reminder after dividing multiplication of array by given number is - ',arr_mul_div(arr1,11))

print('The array given is Monotonic' if check_arr_monotonic(rotate_arr_1(arr1,1)) else 'The array given is NOT Monotonic')
print('The array given is Monotonic' if check_arr_monotonic(arr1) else 'The array given is NOT Monotonic')