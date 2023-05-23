import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data/data.csv')
  get_population_by_country(data)
  get_population_by_percentage(data)

def get_population_by_country(data):
    country = input('Type country => ')
    result = utils.population_by_country(data, country, 'Country/Territory')
    if len(result) > 0:
        labels, values = utils.get_population(result[0])
        charts.generate_bar_chart(labels, values, country)
    else:
        raise Exception('No existe el dato para el pais.')

def get_population_by_percentage(data):
    continent = 'North America'
    labels, values = utils.get_population_by_percentage(data, continent)
    charts.generate_pie_chart(labels, values, continent)

if __name__ == '__main__':
  run()