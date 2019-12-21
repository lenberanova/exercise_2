import functools

def decorator_positive_result(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        assert result >= 0, fn.__name__ + '() result is < 0'
        return result
    return wrapper

@decorator_positive_result
def counting_addition(*args):
    counting_result = 0
    for arg in args:
        counting_result += arg
    return counting_result

@decorator_positive_result
def counting_substraction(*args):
    counting_result = args[0]
    substraction_args = args[1:]
    for arg in substraction_args:
        counting_result -= arg
    return counting_result

@decorator_positive_result
def counting_division(*args):
    try:
        counting_result = args[0]
        division_args = args[1:]
        for arg in division_args:
            counting_result /= arg
        return counting_result
    except ZeroDivisionError as err:
        assert False, 'counting_division() ' + str(err)


a = 2
b = 2
c = 10
x = (10, 2, 5)


counting_addition_result = counting_addition(*x)
print('counting_addition_result = {}'.format(counting_addition_result))

counting_subtraction_result = counting_substraction(*x)
print('counting_subtraction_result = {}'.format(counting_subtraction_result))

counting_subtraction_result2 = counting_substraction(c, a, b)
print('counting_subtraction_result2 = {}'.format(counting_subtraction_result2))

counting_division_result = counting_division(*x)
print('counting_division_result = {}'.format(counting_division_result))

