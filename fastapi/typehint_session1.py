str1  = 'Ramanshu'

print(type(str1))

a = 10

print(type(a))


a = '10'

print(type(a))

print('-'*20)

text: str = "Ramanshu"

text1: str = '1000'

print(type(text))
print(type(text1))

text2: str  = 1000

print(type(text2))

print('-'*20)

def func(param):
    param.reverse()
    return param

print(func(['1','2','3']))


def func1(param: list[str]) -> list[str]:
    param.reverse()
    return param

print(func1(['4','5','6']))

print('-'*20)

def full_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()

print(full_name('ramanshu', 'kharche'))

def full_name1(first_name: str, last_name: str) -> str:
    return first_name.title() + " " + last_name.title()

print(full_name('ramanshu', 'kharche'))

print('-'*20)

"""
Types in Type Hint
1. str
2. int
3. bool
4. bytes
5. float
"""

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

print(get_items('Ramanshu', 23, 5.9, True, b"a"))

print('-'*20)

from typing import Any
def random_func(data: Any):
    return data

print(random_func('Ramanhu'))
print(random_func(100))

print('-'*20)

"""Generic Type
1. list[str]
2. tuple[int, int, int]
3. set[bytes]
4. dict[str, str]
"""
def process_list(items: list[str]) -> None:
    for item in items:
        print(item)

process_list(['1', '2', '3'])


def process_tuple_and_set(item_t: tuple[int, int, str], item_s: set[bytes]):
    return item_t, item_s

print(process_tuple_and_set((1,2,'3'), {b"a"}))

def process_dict(prices: dict[str, int]):
    for item_name, item_price in prices.items():
        print(item_name, ' -> ', item_price)

process_dict({"Bottle":100, 'Glasses':150})

print('-'*20)

"""Union 
Declare variables accepting multiple types using '|' """

def process_id(item: str| int):
    print('ID: ', item, 'of type: ', type(item))

process_id(100)
process_id('Ramanshu')

def greet(name: str | None = None):
    if name is not None:
        print('Hello ', name)
    else:
        print('Welcome to ABC...!')

greet('Ramanshu')
greet()

print('-'*20)

from collections.abc import Iterable

def reverse_array(items: Iterable):
    return list(items)[::-1]

print(reverse_array(['1','2',]))

print('-'*20)

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person) -> str:
    return one_person.name

p = Person('Ram')

print(get_person_name(p))