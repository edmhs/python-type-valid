# python-type-valid

[![Python type valid Build passed](https://travis-ci.org/edmhs/python-type-valid.svg?branch=master)](https://travis-ci.org/edmhs/python-type-valid)
[![Python type valid Code Coverage](https://codecov.io/gh/codecov/example-python/branch/master/graph/badge.svg)](https://codecov.io/gh/edmhs/python-type-valid)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/edmhs/python-type-valid)


Python type validation decorator with hinting

* Validate input DONE
* Validate Output DONE
* Validate input **kwargs ?
* Validate mandatory **kwargs ?
* Multiple types ?

### Types examples

~~~
str ""
int 4
float 10.5
list []
tuple ()
~~~

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

#valid
hello("Bob")

#invalid
hello(1)

@type_valid
def user(name: str, age: int, salary: float) -> str:
    return name+str(age)+str(salary)

#valid
user(name="Bob", age=25, salary=1000.00)

~~~

### Raises TypeError
~~~sh
TypeError: in method 'hello', Argument 'name' is not of type <class 'str'>, received <class 'int'>
~~~
