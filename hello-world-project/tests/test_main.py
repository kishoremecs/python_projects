import unittest
from hello_world.main import get_greeting

class TestMain(unittest.TestCase):
    def test_get_greeting_default(self):
        self.assertEqual(get_greeting(), "Hello, World!")
    
    def test_get_greeting_custom(self):
        self.assertEqual(get_greeting("Python"), "Hello, Python!")

if __name__ == "__main__":
    unittest.main()