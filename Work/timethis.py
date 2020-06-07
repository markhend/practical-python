# timethis.py
import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            func(*args, **kwargs)
        finally:
            end = time.time()
            print(f'{func.__module__}.{func.__name__} : {end-start}')
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    countdown(1000000)

