# before pydantic

class Student:
    def __init__(self, name: str, age: int, gpa: float):
        self.name = name
        self.age = age
        self.gpa = gpa

s = Student(name = 33, age = 'Twenty', gpa = True)
print(s.name, ' ', s.age, ' ', s.gpa)

print('-'*20)

# After pydantic
# It enforce the datatype for specified variable

from pydantic import BaseModel

class Student (BaseModel):
    name:str
    age:int
    gpa:float

s1 = Student(name = 'ramanshu', age = 21, gpa = 2.3)
print(s1)

print('-'*10)

# s2 = Student(name = 33, age = 'Twenty', gpa = True)
# print(s2)
# Here, gpa value is True->1->1.0 sothat it does not raise error bcz of lax mode, pydantic by_default in lax mode

"""    s2 ERROR 
Traceback (most recent call last):
  File "C:\Git_Practice\fastapi\pydantic_session1.py", line 28, in <module>
    s2 = Student(name = 33, age = 'Twenty', gpa = True)
  File "C:\Git_Practice\.venv\Lib\site-packages\pydantic\main.py", line 280, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 2 validation errors for Student
name
  Input should be a valid string [type=string_type, input_value=33, input_type=int]
    For further information visit https://errors.pydantic.dev/2.14/v/string_type
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='Twenty', input_type=str]
    For further information visit https://errors.pydantic.dev/2.14/v/int_parsing
"""

print('-'*20)

# Real World approach, in API data will arrives in Dictionary format.

raw_data = {
    'name':'Ramanshu',
    'age':23,
    'gpa':2.9
}

s2 = Student(**raw_data)
print(s2)

print('-'*20)

raw_data1 ={
    'name':'Shyam',
    'age':'21',
    'gpa':'21.5'
}

s3 = Student(**raw_data1)
print(s3)
print(type(s3.name), type(s3.age), type(s3.gpa))

print('-'*20)

raw_data1 ={
    'name':'Shyam',
    'age':22.5,
    'gpa':'21.5'
}

# s4 = Student(**raw_data1)
# print(s4)
# print(type(s4.name), type(s4.age), type(s4.gpa))

""" s4 ERROR
Traceback (most recent call last):
  File "C:\Git_Practice\fastapi\pydantic_session1.py", line 78, in <module>
    s4 = Student(**raw_data1)
  File "C:\Git_Practice\.venv\Lib\site-packages\pydantic\main.py", line 280, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
age
  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=22.5, input_type=float]
    For further information visit https://errors.pydantic.dev/2.14/v/int_from_float
"""


# ValidationError

from pydantic import ValidationError

raw_data4 = {
    'name': 1234,
    'age':'Ten'
}

try:
    s5 = Student(**raw_data4)
except ValidationError as e:
    print(f'Total number of errorr found:{e.error_count()}')
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")

print('-'*20)

"""
Try writing a small Product (BaseModel) in your notebook with fields: 
product id: int, name: str, price: float, in_stock: bool, and test it with:

Valid coerced inputs (product_id="50", price="199,99", in_stock="1"), 
A broken input inside try / except ValidationError as et and print e.error_count(),
"""

from pydantic import BaseModel, ValidationError
class Product(BaseModel):
    product_id: int
    name: str
    price: float
    in_stock: bool

raw_data5 = {
    "product_id":"50", 
    "price":"199,99",       
    "in_stock":"1"
}

try: 
    p = Product(**raw_data5)
except ValidationError as e:
    print(f'Total number of errors: {e.error_count()}')
    for err in e.errors():
        print(f'Fields {err['loc']}, Type: {err['type']}, Message: {err['msg']}')

# In this example name attribute has no value this is 1st ERROR & price attribute has incorrect data_type this is 2nd ERROR. 

print('-'*50)



from pydantic import BaseModel, ValidationError
class Product(BaseModel):
    product_id: int
    name: str

# Required and Non-nullable
# what happens when value is not provided in dict
value = {
    "product_id":'50'
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error:{e.error_count()}")
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")

print('-'*20)

# Required and Non-nullable
# what happens when value is None

value = {
    "product_id":'50',
    "name": None
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error:{e.error_count()}")
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")

print('-'*20)

from pydantic import BaseModel, ValidationError
class Product(BaseModel):
    product_id: int
    name: str |None

# Required and nullable
# what happens when value is not provided in dict
value = {
    "product_id":'50'
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error:{e.error_count()}")
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")

print('-'*20)

# Required and nullable
# what happens when value is None

value = {
    "product_id":'50',
    "name": None
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error:{e.error_count()}")
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")


#strict mode in pydantic

from pydantic import BaseModel,ConfigDict

class Student(BaseModel):
    model_config = ConfigDict(strict=True)
    age : int

s = Student(age=22)
print(s)


s1 = Student(age='22')  # string data_type ->Error
print(s1)