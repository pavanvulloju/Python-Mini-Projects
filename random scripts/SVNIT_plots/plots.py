import random
import pandas as pd
import matplotlib.pyplot as plt

random.seed(0)
colors_list = ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff", "#a0c4ff", "#bdb2ff", "#ffc6ff"]

k = pd.read_csv('marks.csv')


def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center', Bbox=dict(facecolor='#34a0a4', alpha=1))


for a in k.columns[1:238]:
    try:
        plt.clf()
        plt.ylim(2, 10)
        plt.title(a)
        plt.xlabel('Semester')
        plt.ylabel('CGPA')
        my_colors = random.choices(colors_list, k=9)
        plt.bar(k['RollNo'], k[a], color=my_colors)
        add_labels(k['RollNo'], k[a])
        plt.savefig(f'./Img_plots/{a}.png')

    except Exception as e:
        print(e)


