import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        #print(header)
        data = []
        for row in reader:
            '''
            print('***' * 5)
            print(row)
            '''
            iterable = zip(header, row)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            #print(country_dict)
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./data/data.csv')
    print(data[0])