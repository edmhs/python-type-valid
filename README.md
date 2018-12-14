# python-type-valid

![Python type valid Build passed](https://travis-ci.org/edmhs/python-type-valid.svg?branch=master)

Python type validation decorator with hinting

### Installation
~~~sh
pip install type-valid
~~~

### Usage
~~~python
from type_valid import type_valid

@type_valid
def hello(name: str) -> str:
    return name
    
~~~

### Raises TypeError
~~~sh
TypeError: in method 'hello', Argument 'name' is not of type <class 'str'>, received <class 'int'>
~~~
