#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

search_item = 'cars'
url = 'https://www.facebook.com/marketplace/phoenix/'+search_item
driver.get(url)

#%%
n_scrolls = 2
for _ in range(n_scrolls):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(.5)

#%%
soup = BeautifulSoup(driver.page_source, 'html.parser')

def get_listing_data(soup):
    class_listing = 'x3ct3a4'
    class_price = 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u'
    class_title = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6'
    class_location = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84'

    listings = soup.find_all('div', {"class" : class_listing})
    listing_rows = []
    for listing in listings:
        row = []
        listing_title = listing.find_all(class_ = class_title)
        listing_price = listing.find_all(class_ = class_price)
        listing_location = listing.find_all(class_ = class_location)
        # print(listing_location)
        row.append(listing_title[0].text)
        row.append(listing_price[0].text)
        row.append(listing_location[0].text)
        if len(listing_location) > 1:
            row.append(listing_location[1].text)

        listing_rows.append(row)

    return listing_rows

listing_rows = get_listing_data(soup)
columns = ['title', 'price', 'location', 'mileage']
data = pd.DataFrame(listing_rows, columns = columns)
data

#%%

def clean_data(data):
    dict1 = {
        'Free' : '0',
        '\$': '',
        ',': '',
        'K? miles': '',
        ' · Dealership': '',
    }

    data = data.replace(dict1, regex = True)
    data = data[data['title'].str.contains('[Hh]ot\s?[Ww]heels', regex=True) == False]

    data['mileage'] = data['mileage'].astype(float)
    data['price'] = data['price'].astype(float)

    data = data.dropna(subset=['mileage', 'price'])
    # outlier_index = data[data['price'] > 80000][data['mileage'] > 250].reset_index()['index'][0]
    # data = data.drop([outlier_index], axis = 0)
    return data

clean_data(data)


#%%
path = 'data/' + search_item + '1.csv'
data.to_csv(path, index = False)

# %%
driver.quit()

# %%
import pandas as pd

path = 'census.xlsx'
data = pd.read_excel(path)
data
