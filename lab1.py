#Name: Eric Pirniakan

def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == []:
        return None
    if int_list is None:
        raise ValueError
    max_value = int_list[0]
    for i in int_list:
        if i > max_value:
            max_value = i
    return max_value

def reverse_rec(int_list):   # must use recursion
    if int_list is None:
        raise ValueError
    if int_list == []:
        return None
    if len(int_list) == 1:
        return int_list
    else:
        return [int_list[len(int_list)-1]] + reverse_rec(int_list[:len(int_list)-1])

def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    if int_list == []:
        return None
    if low > high:
        return None
    elif low <= high:
        middle = (low + high) // 2
        if int_list[middle] == target:
            return middle
        elif int_list[middle] > target:
            high = middle - 1
            return bin_search(target, low, high, int_list)
        elif int_list[middle] < target:
            low = middle + 1
            return bin_search(target, low, high, int_list)

