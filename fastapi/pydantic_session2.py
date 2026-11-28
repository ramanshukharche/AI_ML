from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str = "Ramanshu"

# Optional and Non-nullable
# what happens when value is not provided in dict

value = {
    "product_id" : "50"
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f'Total number of error found: {e.error_count()}')
    for err in e.errors():
        print(f'Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}')
 
print('-'*30)
#--------------------------------------------------------------------------------------------------------

from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str = "Ramanshu"

# Optional and Non-Nullable
# what happens if value is None

value = {
    'product_id' : '50',
    'name': None 
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f'Total number of errors found: {e.error_count()}')
    for err in e.errors():
        print(f'Feilds: {err["loc"]}, Type: {err["type"]}, Message: {err["msg"]}')

print('-'*30) 

#===============================================================================================

from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str | None = None

# Optional and Nullable
# what happens when value is not provided in dict
value = {
    'product_id': '50'
}

try: 
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f'Total number of error found: {e.error_count()}')
    for err in e.errors():
        print(f'Fields: {err["loc"]}, Type: {err["type"]}, Message: {err["msg"]}')

print('-'*30)

#--------------------------------------------------------------------------------------------------------

from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str | None = None

# Optional and Nullable
# what happens if value is None

value = {
    'product_id': '50',
    'name': None
}


try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f'Total number of error found: {e.error_count()}')
    for err in e.errors():
        print(f'Fields: {err["loc"]}, Type: {err['type']}, Message: {err["msg"]}')

print('-'*30)

# pydantic does not validate default value by itself.
from pydantic import BaseModel

class Product(BaseModel):
    product_id : int = 'abc'

p = Product()
print(p)

# Here, p object does not have any argument so it uses default argument but we specify int data_type for product_id but default argument have str data_type (LAX mode also not applicable)
# But according to Pydantic Rule -> pydantic does not validate default value by itself sothat it execute without error with default value

print('<<-'*30)

from pydantic import BaseModel
from datetime import datetime, UTC
import time

class BadExample(BaseModel):
    created_dt: datetime = datetime.now(UTC)        # this creates the value once when the class is defined.

b1 = BadExample()
time.sleep(2)
b2 = BadExample()

print(b1)
print(b2)
print(b1.created_dt == b2.created_dt)   # always true 

print('+'*60)

# correct example

from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, UTC
import time

class GoodExample(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory= lambda: datetime.now(UTC))        # creates a new value every time an object is created.

g1 = GoodExample()
time.sleep(2)
g2 = GoodExample()

print(g1)
print(g2)
print(g1.created_at == g2.created_at)   # always false

print('-+'*30) 

from datetime import datetime, UTC
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class LLMChatRequest(BaseModel):
    # Required
    prompt: str

    # Optional with sensible production defaults
    model: str = 'gpt-40-mini'
    temperature: float = 0.7
    max_tokens: int | None = None
    system_sequence: str | None = None
    stop_sequences: list[str] =  Field(default_factory=list)

    # Auto-generated metadata per request
    trace_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

req = LLMChatRequest(prompt="Explain RAG in 2 sentences.")
print(req)

req.stop_sequences.append("Hello Stop Here...!")
print(req)

print('-<<-'*30)

class Prompt(BaseModel):
    text: str = Field(description="User text value")
    user_id: str = Field(...,description="Caller user id")      # ..., makes  field mandatory
    value: str | None = Field(default=None, description="random value")

print(Prompt(text='abc', user_id='pqr', value=None))
# print(Prompt(user_id='pqr'))  # Que: Why it wont work if text and value is optional and user_id is mandatoty(required)

print('-><-'*30)

# How to validate default value

class ValidateVal(BaseModel):
    product_id: int = Field(default='xyz', validate_default=True)

try:
    ValidateVal()
except ValidationError as e:
    print(e.errors()[0]['msg'])

# Dynamic data assign
class ModelData(BaseModel):
    model_name: str
    version: int = 1
    attribute_val: str = Field(
        default_factory=lambda data: f'{data['model_name']}: {data["version"]}'
    )

s = ModelData(model_name='gpt')
print(s)


# Question for students 
"""
Create an ExperimentRun(BaseModel) for an ML training tracker with:

experiment_name: str (required, non-nullable)
parent_run_id: str | None (required key, can be None)
learning_rate: float = 0.001 (optional, non-nullable)
run_id: UUID (auto-generated fresh UUID per instance via default_factory)
metrics: dict[str, float] (defaults to a fresh empty dict {} via default_factory)

Test creating 2 separate runs and verify run1.run_id != run2.run_id!
"""

# from pydantic import BaseModel,Field
# from uuid import UUID, uuid4

# class ExperimentRun(BaseModel):
#     experiment_name: str
#     parent_run_id: str | None
#     learning_rate: float = 0.001
#     run_id: UUID = Field(default_factory=uuid4)
#     metrics: dict[str, float] = Field(default_factory=dict)


# run1 = ExperimentRun(
#     experiment_name="Model Training",
#     parent_run_id=None
# )

# run2 = ExperimentRun(
#     experiment_name="Model Testing",
#     parent_run_id="RUN101"
# )

# print(run1)
# print(run2)

# print(run1.run_id != run2.run_id)