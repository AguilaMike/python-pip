import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, country = ''):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    save_chart_as_image(f'./images_charts/{country}_bar.png')

def generate_pie_chart(labels, values, continent = ''):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    save_chart_as_image(f'./images_charts/{continent}_pie.png')

def save_chart_as_image(extension):
    plt.savefig(extension)
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)