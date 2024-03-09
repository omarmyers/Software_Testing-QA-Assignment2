import unittest
from main import calculate_bmi, get_bmi_category


class TestBMI(unittest.TestCase):

  def test_calculate_bmi(self):
    # Normal input
    self.assertAlmostEqual(calculate_bmi(5,3,150), 27.2,delta=0.1)
    
    # Small input
    self.assertAlmostEqual(calculate_bmi(0,1,1), 720, delta=0.1)
    
    # Large input
    self.assertAlmostEqual(calculate_bmi(10,11,1000), 42, delta=0.1)

  def test_get_bmi_category(self):
    # Tests for Underweight category
    self.assertEqual(get_bmi_category(0), "Underweight")
    self.assertEqual(get_bmi_category(18.49), "Underweight")

    # Tests for Normal weight category
    self.assertEqual(get_bmi_category(18.5),"Normal weight")
    self.assertEqual(get_bmi_category(24.99),"Normal weight")

    # Tests for Overweight category
    self.assertEqual(get_bmi_category(25),"Overweight")
    self.assertEqual(get_bmi_category(29.99),"Overweight")

    # Tests for Obese category
    self.assertEqual(get_bmi_category(30),"Obese")
    self.assertEqual(get_bmi_category(100),"Obese")

if __name__ == '__main__':
  unittest.main()
