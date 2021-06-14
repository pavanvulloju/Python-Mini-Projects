import re
import os
import matplotlib.pyplot as plt

regex = "\d.*m\s-\s.*:\s"
name_regex = "m\s-\s.*?:"


class WhatsappAnalyse:
	name_set = {}

	def __init__(self, file_name):
		self.file_name = file_name

	def read_chat(self):
		with open(self.file_name, 'r', encoding='utf-8') as f:
			data = f.read()
		return data

	def get_data(self):
		for a in re.findall(regex, self.read_chat()):
			for b in re.findall(name_regex, a):
				name = b.lstrip('m - ').rstrip(':')
				if name not in self.name_set.keys():
					self.name_set[name] = 0
				self.name_set[name] += 1
		return self.name_set

	def plot_graph(self):

		member_dict = self.get_data()
		name = list(member_dict.keys())
		messages = list(member_dict.values())

		plt.figure(figsize=(15, 10))

		# creating bar charts and labels for the chart
		if len(member_dict) < 30:
			plt.bar(name, messages, color='#069AF3', width=0.4)
			plt.xticks(rotation=30)
		else:
			plt.bar(name, messages, color='#069AF3', width=0.4, align='center')
			plt.xticks(rotation=90, fontsize=5)

		plt.xlabel("Name")
		plt.ylabel("No. of Messages")
		plt.title('No.of Messages in ' + self.file_name)
		plt.savefig(self.file_name.strip('.txt') + '.png')
		self.name_set.clear()


if __name__ == '__main__':
	group_chat_list = []

	for element in os.listdir():
		if element.startswith('WhatsApp Chat with') and element.endswith('.txt'):
			group_chat_list.append(element)

	if group_chat_list:
		for file in group_chat_list:
			object_name = WhatsappAnalyse(file)
			object_name.plot_graph()
