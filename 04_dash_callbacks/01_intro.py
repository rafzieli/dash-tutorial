def dekorator(func):
    return func

def hello_world():
    return print('Hello World')

hello_world_dekorator = dekorator(hello_world)


print(type(hello_world_dekorator))

hello_world_dekorator()