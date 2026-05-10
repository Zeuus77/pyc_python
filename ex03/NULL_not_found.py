def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
        return 0
    if type(object) is float and object != object:
        print("Cheese: nan <class 'float'>")
        return 0
    if type(object) is int and object == 0:
        print("Zero: 0 <class 'int'>")
        return 0
    if type(object) is str and object == "":
        print("Empty: <class 'str'>")
        return 0
    if object is False:
        print("Fake: False <class 'bool'>")
        return 0
    print("Type not Found")
    return 1