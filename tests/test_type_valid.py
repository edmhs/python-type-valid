import unittest
from type_valid.type_valid import type_valid


class TestTypeValid(unittest.TestCase):

    def setUp(self):
        @type_valid
        def name_str(username: str):
            return username

        @type_valid
        def name_str_2(username: str) -> str:
            return 1

        @type_valid
        def name_int(age: int) -> int:
            return age

        @type_valid
        def multi(age: int, name: str, salary: float):
            return name+str(age)+str(salary)

        self.name_str = name_str
        self.name_str_2 = name_str_2
        self.name_int = name_int
        self.multi = multi

    def test_string_valid(self):
        self.assertEqual(self.name_str(username="myString"), "myString")

    def test_string_invalid_return(self):
        with self.assertRaises(TypeError):
            self.name_str_2(username="bob")

    def test_string_invalid_int(self):
        with self.assertRaises(TypeError):
            self.name_str(username=1)

    def test_string_invalid_bool(self):
        with self.assertRaises(TypeError):
            self.name_str(username=True)

    def test_int_valid(self):
        self.assertEqual(self.name_int(age=15), 15)

    def test_int_invalid_string(self):
        with self.assertRaises(TypeError):
            self.name_int(age="5")

    def test_multi_valid(self):
        self.assertEqual(self.multi(name="python", age=15, salary=100.00),
                         "python15100.0")

    def test_multi_invalid(self):
        with self.assertRaises(TypeError):
            self.multi(name="python", age="15", salary=100.00)
