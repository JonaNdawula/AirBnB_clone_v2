#!/usr/bin/python3
"""doc doc"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """doc doc """

    def __init__(self, *args, **kwargs):
        """doc doc """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """doc doc """
        new = self.value()
        self.assertEqual(type(new.name), str)
