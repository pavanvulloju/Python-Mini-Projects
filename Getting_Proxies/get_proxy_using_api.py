import requests


class GetProxies:
	DEFAULT_NUM_PROXIES = 15

	def __init__(self, no_of_proxies_required):
		self.no_of_proxies_required = no_of_proxies_required

	def get_response(self):
		if self.no_of_proxies_required < self.DEFAULT_NUM_PROXIES:
			api_url = f'https://www.proxyscan.io/api/proxy?format=json&limit={self.no_of_proxies_required}'
			response = requests.get(api_url).json()
		else:
			api_url = f'https://www.proxyscan.io/api/proxy?format=json&limit={self.DEFAULT_NUM_PROXIES}'
			print('we are processing only 15 proxies max for now!!!')
			response = requests.get(api_url).json()

		return response

	def get_proxies(self):
		json_response = self.get_response()
		proxy_list = []

		for i in range(len(json_response)):
			ip_address = json_response[i]["Ip"]
			port_number = json_response[i]["Port"]
			proxy = f'{ip_address}:{port_number}'
			proxy_list.append(proxy)
		return proxy_list


my_proxy = GetProxies(19)
print(my_proxy.get_proxies())
