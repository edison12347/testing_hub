def max(*args, **kwargs):
    # key arguement wasn't passed
    if len(args) > 1:
        input_list = list(args)
    else:
        input_list = list(*args)
    try:
        # key was passed in kwargs
        print(input_list)
        key_func = kwargs['key']
        max_key = key_func(sorted(input_list)[-1])
        for val in input_list:
            if key_func(val) == max_key:
                return val
    except KeyError:
        # there is not key
        return sorted(input_list)[-1]


def min(*args, **kwargs):
    # key arguement wasn't passed
    if len(args) > 1:
        input_list = list(args)
    else:
        input_list = list(*args)
    try:
        # key was passed in kwargs
        print(input_list)
        key_func = kwargs['key']
        print(sorted(input_list)[0])
        min_key = key_func(sorted(input_list)[0])
        print(min_key)
        for val in input_list:
            if key_func(val) == min_key:
                return val
    except KeyError:
        # there is not key
        return sorted(input_list)[0]

print(min([[3, 4], [1, 2], [5, 4], [9, 0]], key=lambda x: x[1]))  # = [9, 0]