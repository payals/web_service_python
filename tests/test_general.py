import unittest
import urllib2
import json

class serv_test(unittest.TestCase):

	def _RestClientGet(self, param):
		"""extraxt input from URL and generate fibonacci series of that length"""
		url = "http://localhost:8080/%s" % (param)
		response = urllib2.urlopen(url)
		return json.loads(response.read())

	def test_1(self):
		response_data = self._RestClientGet("fibonacci/1")
		expected_data = {u"fib_series": [0]}
		self.assertEqual(response_data, expected_data)

	def test_2(self):
		response_data = self._RestClientGet("fibonacci/2")
		expected_data = {u"fib_series": [0, 1]}
		self.assertEqual(response_data, expected_data)

	def test_3(self):
		response_data = self._RestClientGet("fibonacci/3")
		expected_data = {u"fib_series": [0, 1, 1]}
		self.assertEqual(response_data, expected_data)

	def test_4(self):
		response_data = self._RestClientGet("fibonacci/4")
		expected_data = {u"fib_series": [0, 1, 1, 2]}
		self.assertEqual(response_data, expected_data)

	def test_negative_input(self):
		response_data = self._RestClientGet("fibonacci/-4")
		self.assertListEqual(response_data.keys(), [u"Exception"])

	def test_zero_input(self):
		response_data = self._RestClientGet("fibonacci/0")
		self.assertListEqual(response_data.keys(), [u"Exception"])

	def test_upper_limit(self):
		response_data = self._RestClientGet("fibonacci/1004")
		self.assertListEqual(response_data.keys(), [u"Exception"])

	def test_float_input(self):
		response_data = self._RestClientGet("fibonacci/1.33")
		self.assertListEqual(response_data.keys(), [u"Exception"])

	def test_string_input(self):
		response_data = self._RestClientGet("fibonacci/payal")
		self.assertListEqual(response_data.keys(), [u"Exception"])



def suite():
	serv_test = unittest.TestLoader().loadTestsFromTestCase(serv_test)
	return serv_test

if __name__ == '__main__':
	unittest.main()
