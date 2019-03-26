def add(x,y):
    try:
        return(x+y)
    except TypeError:
        raise TypeError("x and y must be either numbers, lists, or strings, and of the same type") from None
