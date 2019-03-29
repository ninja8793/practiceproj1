

def numbers_to_strings(argument,a,b):
    switcher = {
        1: a+b,
        2: a-b,
        3: a*b,
        4: a/b,

    }
    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    print(numbers_to_strings(1,2,3))