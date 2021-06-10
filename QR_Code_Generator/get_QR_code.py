# This QR code works for only 24 hours because it is cached for only 1 day at the servers of the QRTAG (qrtag.net/api)
# This code lets you to go to your required URLs by scanning QR codes
# Version 1.0

import requests
import os


class QRCode:
	def __init__(self, url, download_type, pixel_size, qr_code_name):
		self.url = url  # eg., https://en.wikipedia.org/ , https://github.com ......
		self.download_type = download_type  # png, svg
		self.pixel_size = pixel_size  # 2,3,...12(max)
		self.qr_code_name = qr_code_name

	def get_qr(self):
		response = requests.get(f'https://www.qrtag.net/api/qr_{self.pixel_size}.{self.download_type}?url={self.url}')
		qrcode = response.content
		return qrcode

	def download_qr(self):
		result = self.get_qr()
		path = os.path.join(os.getcwd(), f'downloads')
		if not os.path.exists(path):
			os.mkdir(path)

		with open(path + f'\\{self.qr_code_name}.{self.download_type}', 'wb') as f:
			f.write(result)


if __name__ == '__main__':
	user_url = input("Type a URL or paste it here: ")
	file_type = input("Enter file type (png/svg): ")
	ur_size = int(input("Enter the pixel size of the QR (maximum 12): "))
	file_name = input("Enter the name of the QR Code: ")

	my_qr = QRCode(user_url, file_type, ur_size, file_name)
	my_qr.download_qr()
