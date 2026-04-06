def names():
    all_names = []

    def inner(name: str) ->list:
        all_names.append(name)
        return all_names
    
    return inner

def average():
    values = []

    def inner(value: int) -> float:
        values.append(value)
        return sum(values) / len(values)
    
    return inner


if __name__ =="__main__":
    avg = average()
    print(avg(10))
    print(avg(30))
    print(avg(20))

""" boys = names()
    girls = names("
    print(boys("q ")
    print(boys("w"")
    print(boys("e ")
    print(girls("d")
    print(girls("z")
    print(girls("x")
    print(girls("c")"""
