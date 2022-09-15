from functools import wraps
from time import perf_counter, time
from linked_list_iterator import LinkedList

def timer(funct):
        @wraps(funct)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            res = funct(*args, **kwargs)

            duration = perf_counter() - start
            print(f'[{wrapper.__name__}] took {duration * 1000} ms')
            return res
        return wrapper

@timer
def foods():
    foods = LinkedList(("apple","banana","cucumber"))

    foods_list = []

    for food in foods:
        foods_list.append(food)
    return foods_list

if __name__ == "__main__":
    test = foods()
    print(test)