import unittest
from type_valid.type_valid import type_valid


class TestTypeValid(unittest.TestCase):

    def setUp(self):
        @type_valid
        def name_str(username: str) -> str:
            return username

        @type_valid
        def name_int(age: int) -> int:
            return age

        self.name_str = name_str
        self.name_int = name_int

    def test_string_valid(self):
        self.assertEqual(self.name_str(username="myString"), "myString")

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
