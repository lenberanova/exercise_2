def decorator_positive_result(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        assert result >= 0, fn.__name__ + '() result is < 0'
        return result
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper

@decorator_positive_result
def counting(a, b):
    result = a + b
    return result

x = counting(1, -3)
print('x = {}'.format(x))