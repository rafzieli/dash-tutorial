def dekorator(func):
    def wrapper():
        func()
        print('Wywolanie funkcji wrapper')
    return wrapper

@dekorator
def function_2():
    print('Wywolanie funkcji func_2')
    
function_2()

