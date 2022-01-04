import unittest2
from statusPage import StatusPage
from HtmlTestRunner import HTMLTestRunner

class TestCliengo(unittest2.TestCase):
	def setUp(self):
		self.base_url = "https://beta-blog.cliengo.com"
		self.status = StatusPage(self.base_url)


	def test_response_article1(self):
		self.assertEqual(self.status.response_article1(), 200)


	def test_response_article2(self):
		self.assertEqual(self.status.response_article2(), 200)


	def test_response_article3(self):
		self.assertEqual(self.status.response_article3(), 200)


	def test_response_article4(self):
		self.assertEqual(self.status.response_article4(), 200)


	def test_response_article5(self):
		self.assertEqual(self.status.response_article5(), 200)


	def tearDown(self):
		pass


if __name__ == "__main__":
	unittest2.main(testRunner=HTMLTestRunner(output="reports"))
