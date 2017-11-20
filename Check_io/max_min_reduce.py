from functools import reduce


def max(*args, **kwargs):
    if len(args) > 1:
        input_list = list(args)
    else:
        input_list = list(*args)
    if len(kwargs) == 0:
        # has  no kwargs
        return reduce(lambda a, b: a if (a >= b) else b, input_list)
    else:
        # there are some kwargs
        try:
            key_func = kwargs['key']
            return reduce(lambda a, b: a if (key_func(a) >= key_func(b)) else b, input_list)
        except KeyError:
            # key arguement wasn't passed
            return 'plz provide valid key'
        except TypeError:
            return 'provided value of the key attribute is not valid!!!11 plz provide correct'


def min(*args, **kwargs):
    if len(args) > 1:
        input_list = list(args)
    else:
        input_list = list(*args)
    if len(kwargs) == 0:
        # has  no kwargs
        return reduce(lambda a, b: a if (a <= b) else b, input_list)
    else:
        # there are some kwargs
        try:
            key_func = kwargs['key']
            return reduce(lambda a, b: a if (key_func(a) <= key_func(b)) else b, input_list)
        except KeyError:
            # key arguement wasn't passed
            return 'plz provide valid key'
        except TypeError:
            return 'provided value of the key attribute is not valid!!!11 plz provide correct'