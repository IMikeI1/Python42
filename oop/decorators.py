'''
Дикаратор - это функция, которая позволяет изменять или расширять поведение другой функций или метода
'''
import time


def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def repeat(num_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_time):
                func(*args, **kwargs)
        return wrapper
    return decorator

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"время проведения: {end - start}")
        return result
    return wrapper


@decorator
def hello():
    print("Hello")

def greet(name):
    print(f" Hello, {name}")

@timing
def parse_page():
    time.sleep(3)

def memoize(func):
    cashe = {}
    def wrapper(*args):
        if args in cashe:
            return cashe[args]
        else:
            result = func(*args)
            cashe[args] = result
            return result
    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# hello()
# greet(name="Alisa")
# parse_page()
start = time.time()
print(fibonacci(60))
end = time.time()
print(f"время проведения: {end - start}")