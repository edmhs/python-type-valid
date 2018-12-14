import unittest
from type_valid.type_valid import type_valid


class TestTypeValid(unittest.TestCase):

    def test_string_valid(self):
        @type_valid
        def name(username: str) -> str:
            return username
        self.assertEqual(name(username="myString"), "myString")

    def test_string_invalid_int(self):
        @type_valid
        def name(username: str) -> str:
            return username
        with self.assertRaises(TypeError):
            name(1)

    def test_string_invalid_bool(self):
        @type_valid
        def name(username: str) -> str:
            return username
        with self.assertRaises(TypeError):
            name(True)

    def test_int_valid(self):
        @type_valid
        def name(age: int) -> int:
            return age
        self.assertEqual(name(age=15), 15)

    def test_int_invalid_string(self):
        @type_valid
        def name(age: int) -> int:
            return age
        with self.assertRaises(TypeError):
            name(age="5")
