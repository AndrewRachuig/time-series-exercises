import pandas as pd
import requests
import os

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


def get_power_systems():
    power_systems = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    return power_systems

def main():
    if os.path.isfile('codeup_api_items.csv'):
        items = pd.read_csv('codeup_api_items.csv')
    else:
        items = get_items('https://api.data.codeup.com/api/v1/items')
        items.to_csv('codeup_api_items.csv', index=False)
    
    if os.path.isfile('codeup_api_stores.csv'):
        stores = pd.read_csv('codeup_api_stores.csv')
    else:
        stores = get_stores('https://api.data.codeup.com/api/v1/stores')
        stores.to_csv('codeup_api_stores.csv', index=False)
    
    if os.path.isfile('codeup_api_sales.csv'):
        sales = pd.read_csv('codeup_api_sales.csv')
    else:
        sales = get_sales('https://api.data.codeup.com/api/v1/sales')
        sales.to_csv('codeup_api_sales.csv', index=False)

    comp_df = items.set_index('item_id').join(sales.set_index('item'))
    final_df = comp_df.set_index('store').join(stores.set_index('store_id'))
    return final_df

if __name__ == "__main__":
    main()