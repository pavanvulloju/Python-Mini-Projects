# This is one of the method for getting the required number of proxies
# ------------->  METHOD 1
import requests
import random


class ProxyScraper:
	PROXY_LIST_URL = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'
	no_of_proxies = 20

	def __init__(self, user_req_proxies):
		self.user_req_proxies = user_req_proxies

	def get_proxy_list(self):
		response = requests.get(self.PROXY_LIST_URL).text.split('\n')
		return response

	def check_working_proxies(self):
		working_proxies = []
		for proxy in self.get_proxy_list():
			try:
				if len(working_proxies) < self.user_req_proxies:
					if requests.get('https://www.google.com', proxies={"https://": proxy}, timeout=2).status_code == 200:
						working_proxies.append(proxy)

				else:
					break

			except ConnectionError:
				pass

		return working_proxies

	def get_random_working_proxy(self):
		if self.user_req_proxies > self.no_of_proxies:
			print("Sorry we are serving Maximum 15 Proxies Only")
			self.user_req_proxies = 15
		return random.choices(self.check_working_proxies(), k=self.user_req_proxies)


if __name__ == '__main__':
	required_no_proxies = int(input('How many working proxies do you need (less than 15): '))
	myScrapper = ProxyScraper(required_no_proxies)
	print(myScrapper.get_random_working_proxy())
