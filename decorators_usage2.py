import functools

def decorator_positive_result(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        assert result >= 0, fn.__name__ + '() result is < 0'
        return result
    return wrapper

@decorator_positive_result
def counting(a, b):
    counting_result = a + b
    return counting_result

x = counting(1, 33)
print('x = {}'.format(x))