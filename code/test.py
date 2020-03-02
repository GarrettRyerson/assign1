import unittest
import funcs

class TestStuff(unittest.TestCase):
  def setUp(self):
    pass
  
  def test_product(self):
    self.assertEqual(funcs.product(3,5),15)

if __name__ == "__main__":
  unittest.main()
