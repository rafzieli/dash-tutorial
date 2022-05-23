from datetime import datetime

def dekorator(func):
    def wrapper():
        if 13 <= datetime.now().hour <= 17:
            func()
        else:
            pass
    return wrapper

@dekorator
def pora_dnia():
    print('Wywolanie pora_dnia')
    print('Godziny robocze')

pora_dnia()