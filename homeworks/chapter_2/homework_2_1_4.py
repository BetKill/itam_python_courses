str_, int_, float_ = 0, 0, 0


def cheak(arg):
    global str_, int_, float_
    if isinstance(arg, int) == 1:
        int_ += 1
    elif isinstance(arg, float) == 1:
        float_ += 1
    else:
        str_ += 1
    return str_, int_, float_


def debug_control(*args, **kwargs):
    for i in args:
        cheak(i)
    for j, x in kwargs.items():
        cheak(x)
    return {'str': str_, 'int': int_, 'float': float_}


print(*debug_control("Hello!", 1000, 7, 993.0, name="Petr", task="Eliminate"))