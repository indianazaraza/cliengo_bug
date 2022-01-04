import requests

class BasePage():
	"""Base class for all pages object
	"""
	def __init__(self, base_url):
		"""Initialize an driver

		:param base_url: url to connect to a web page
		:type base_url: str
		"""
		self.base_url = base_url


	def get_status_code(self, locator):
		"""Get an status code from the current request 

		:param locator: endpoint to locate a web page
		:type locator: str
		:rtype: int	
		:return: http code
		"""
		return requests.get(self.base_url + locator).status_code