#!/usr/bin/env python3
# Test the objects module

# Import stuff
import unittest
import objects

class TestObjects(unittest.TestCase):
    def test_get_value_flat_obj(self):
        """Check if objects.get_value() can retrieve values from a flat object"""
        flat_obj = {
            "name": "Forester",
            "brand": "Subaru",
            "body_style": "SUV",
        }
        key = "body_style"
        self.assertEqual(objects.get_value(flat_obj, key), "SUV", "Should return SUV")

    def test_get_value_nested_obj(self):
        """Check if objects.get_value() can retrieve values from nested object"""
        nested_obj = {
            "Forester": {
                "brand": "Subaru",
                "body_style": "SUV",
                "engine": {
                    "type": "boxer",
                    "name": "EJ20",
                    "torque_nm": 138,
                },
            },
        }
        key = "torque_nm"
        self.assertEqual(objects.get_value(nested_obj, key), 138, "Should return 138")

if __name__ == "__main__":
    unittest.main()
