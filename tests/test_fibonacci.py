import unittest
import fibonacci

class test_fibonacci(unittest.TestCase):
	def test_1(self):
		self.assertEqual(fibonacci.fibonacci(1), [0])

	def test_2(self):
		self.assertEqual(fibonacci.fibonacci(2), [0,1])

	def test_3(self):
		self.assertEqual(fibonacci.fibonacci(3), [0,1,1])

	def test_negative(self):
		self.assertRaisesRegexp(ValueError, "less than one", fibonacci.fibonacci, -1)

	def test_zero(self):
		self.assertRaisesRegexp(ValueError, "less than one", fibonacci.fibonacci, 0)

	def test_max(self):
		self.assertRaisesRegexp(ValueError, "maximum", fibonacci.fibonacci, 1001)

	def test_float(self):
		self.assertRaisesRegexp(ValueError, "not integer", fibonacci.fibonacci, 3.14)

	def test_string(self):
		self.assertRaisesRegexp(ValueError, "not integer", fibonacci.fibonacci, "hi")


class test_valid_input(unittest.TestCase):
	def test_valid_input_number(self):
		self.assertTrue(fibonacci.valid_input(25))

	def test_string(self):
		self.assertFalse(fibonacci.valid_input("payal"))


def suite():
	test = unittest.TestLoader().loadTestsFromTestCase(test_valid_input)
	test.loadTestsFromTestCase(test_fibonacci)
	return test

if __name__ == '__main__':
	unittest.main()
