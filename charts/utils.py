def get_population(data_country):
    data = {}
    for key, value in data_country.items():
        if 'Population' in key and key[:4].isdigit():
            data[key[:4]] = int(value)
    return data.keys(), data.values()

def population_by_country(data, country, column_filter):
    return list(filter(lambda item: item[column_filter] == country, data))

def get_population_by_percentage(data, continent=''):
    if continent != '':
        data = list(filter(lambda item: item['Continent'] == continent, data))
    result = {
        row['Country/Territory'] : float(row['World Population Percentage']) 
        for row in data
    }
    return result.keys(), result.values()