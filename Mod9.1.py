def apply_all_func(list_num, *funcs):
    result = {}
    for i in funcs:
        result.update({i.__name__: i(list_num)})
    return result

def minimum(list_num):
    min = list_num[0]
    for i in list_num:
        if min > i:
            min = i
    return min

def maximum(list_num):
    max = list_num[0]
    for i in list_num:
        if max < i:
            max = i
    return max

def lenght(list_num):
    return len(list_num)

def summ(list_num):
    sum_ = 0
    for i in list_num:
        sum_ += i
    return sum_

def sort_ascend(list_num):
    list_num = sorted(list_num)
    return list_num


def sort_descend(list_num):
    list_num = sorted(list_num, reverse=True)
    return list_num

print(apply_all_func([1, 5, 4, 2, 9], minimum, maximum, lenght, summ, sort_ascend, sort_descend))