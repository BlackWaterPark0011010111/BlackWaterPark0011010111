def typed_int(function):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("We need int")
        return function(*args)
    return wrapped

def typed_str(function):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError("We need str")
        return function(*args)
    
    return wrapped

@typed_int
def calculate(a, b, c):
    return a + b + c

if __name__=="__main__":
    print(calculate(1, 2, 3))