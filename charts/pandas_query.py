import pandas as pd

def get_population_by_percentage(continent):
    df = pd.read_csv('./data/data.csv')
    df = df[df['Continent'] == continent]
    labels = df['Country/Territory'].values
    values = df['World Population Percentage'].values
    return labels, values