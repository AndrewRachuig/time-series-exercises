import pandas as pd
import requests

def get_items(starting_url):
    items_list = []
    url = None
    
    while True:
        if url == None:
            url = starting_url
        else:
            response = requests.get(url)
            data = response.json()
            items_list.extend(data['payload']['items'])
            if data['payload']['next_page'] != None:
                url = 'https://api.data.codeup.com' + data['payload']['next_page']
            else:
                return pd.DataFrame(items_list)

items = get_items('https://api.data.codeup.com/api/v1/items'))

def get_stores(starting_url):
    stores_list = []
    url = None
    
    while True:
        if url == None:
            url = starting_url
        else:
            response = requests.get(url)
            data = response.json()
            stores_list.extend(data['payload']['stores'])
            if data['payload']['next_page'] != None:
                url = 'https://api.data.codeup.com' + data['payload']['next_page']
            else:
                return pd.DataFrame(stores_list)

stores = get_stores('https://api.data.codeup.com/api/v1/stores')

def get_sales(starting_url):
    sales_list = []
    url = None
    
    while True:
        if url == None:
            url = starting_url
        else:
            response = requests.get(url)
            data = response.json()
            sales_list.extend(data['payload']['sales'])
            if data['payload']['next_page'] != None:
                url = 'https://api.data.codeup.com' + data['payload']['next_page']
                print(f'next_page is: {url}')
            else:
                return pd.DataFrame(sales_list)

sales = get_sales('https://api.data.codeup.com/api/v1/sales')

items.to_csv('codeup_api_items', index=False)
stores.to_csv('codeup_api_stores', index=False)
sales.to_csv('codeup_api_sales', index=False)

comp_df = items.set_index('item_id').join(sales.set_index('item'))
final_df = comp_df.set_index('store').join(stores.set_index('store_id'))

power_systems = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')