from typing import Type
import unittest


class TestCase(unittest.TestCase):
    def assertEqual(self, first, second, msg=None):
        if first != second:
            if msg is None:
                msg = f'{repr(first)} != {repr(second)}'
            self.fail(msg)
        else:
            super().assertEqual(first, second, msg)

    def _test_initialization(self, class_: Type, attributes: dict):
        if "self" in attributes:
            attributes.pop("self")

        object = class_(**attributes)
        for attr in attributes:
            self.assertEqual(getattr(object, attr), attributes[attr])
        print(object)
        return object
