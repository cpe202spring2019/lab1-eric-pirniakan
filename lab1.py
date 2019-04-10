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

'''def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
''' 
