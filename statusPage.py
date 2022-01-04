from locators import Locators
from basePage import BasePage

class StatusPage(BasePage):
	"""Class that obtains the status code of the page
	"""
	def __init__(self, base_url):
		super().__init__(base_url)


	def response_article1(self):
		"""Get the article 1 status code 

		:rtype: int
		:return: HTTP code
		"""
		return self.get_status_code(Locators.article1)


	def response_article2(self):
		"""Get the article 2 status code 

		:rtype: int
		:return: HTTP code
		"""
		return self.get_status_code(Locators.article2)


	def response_article3(self):
		"""Get the article 3 status code 

		:rtype: int
		:return: HTTP code
		"""
		return self.get_status_code(Locators.article3)


	def response_article4(self):
		"""Get the article 4 status code 

		:rtype: int
		:return: HTTP code
		"""
		return self.get_status_code(Locators.article4)


	def response_article5(self):
		"""Get the article 5 status code 

		:rtype: int
		:return: HTTP code
		"""
		return self.get_status_code(Locators.article5)



