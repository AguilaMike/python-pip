import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # print('status_code =>', r.status_code)
    # print('text =>', type(r.text), r.text)
    categories = r.json()
    print('categories =>', categories)
    print('***' * 10)
    for category in categories:
        print(category['name'])

if __name__ == '__main__':
    get_categories()