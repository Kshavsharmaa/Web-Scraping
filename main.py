import requests
from bs4 import BeautifulSoup
import pandas as pd  # Only import pandas lib For save csv files 

# url = 'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
# html_code = requests.get(url).content
# # print(html_code)

# soup = BeautifulSoup(html_code, 'lxml')
# # print(soup)

# # SCRAPE FOR FIRST DATA FROM THE WEBSITE---------------------------------------------

# # # Scrape all Data using Find_all Method
# # # phone = soup.find_all('div', class_ = '_3pLy-c row')
# # # print(phone)

# # # Scrape First Data using Find Method
# # phone = soup.find('div', class_ = '_3pLy-c row')
# # # print(phone)

# # name = phone.find('div', class_ = '_4rR01T').get_text()
# # print(name)

# # # Get Price of the phone
# # price = phone.find('div', class_ = '_30jeq3 _1_WHN1').get_text()
# # # print(price)

# # # Then Convert price str to int
# # price = int(phone.find('div', class_ = '_30jeq3 _1_WHN1').get_text().replace('₹','').replace(',',''))
# # print(price)
# # # print(type(price))

# # # Get Rating of the phone
# # rating = phone.find('div', class_ = '_3LWZlK').get_text()
# # # print(rating)

# # # Then Converting rating str to float
# # rating = float(phone.find('div', class_ = '_3LWZlK').get_text())
# # print(rating)
# # print(type(rating))

# # # Get Specification of the phone
# # Specification = phone.find('ul', class_ = '_1xgFaf').get_text()
# # print(Specification)
# # # print(type(Specification))  #Already String Format Specification

# # print(name)
# # print(price)
# # print(rating)
# # print(Specification)

# # SCRAPE ALL DATA FROM THE WEBSITES----------------------------------------------------------------------------------

# phones = soup.find_all('div', class_ = '_3pLy-c row')
# for phone in phones:
#     names = phone.find('div', class_ = '_4rR01T').get_text()
#     prices = int(phone.find('div', class_ = '_30jeq3 _1_WHN1').get_text().replace('₹','').replace(',',''))
#     # Specifications = phone.find('ul', class_ = '_1xgFaf').get_text()
#     ratings = float(phone.find('div', class_ = '_3LWZlK').get_text())
    
#     print(names)
#     print(prices)
#     # print(Specifications)
#     print(ratings)
    


# Scrape Data from The all pages from the Websites using For loops

flipkart_phones = {}
names_list = []
prices_list = []
speci_list = []
ratings_list = []

for page in range (1,11):
    url_2 = f'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}'
    html_code = requests.get(url_2).content
    soup = BeautifulSoup(html_code, 'lxml')

#  -------------------------------SCRAPPING------------------------------

    phones = soup.find_all('div', class_ = '_3pLy-c row')
    for phone in phones:
        
        names = phone.find('div', class_ = '_4rR01T').get_text()
        prices = int(phone.find('div', class_ = '_30jeq3 _1_WHN1').get_text().replace('₹','').replace(',',''))
        Speci = phone.find('ul', class_ = '_1xgFaf').get_text()

        try:
            ratings = phone.find('div', class_ = '_3LWZlK').get_text()
        except:
            if (ratings==None):
                print('No Ratings Given')
            

        # print(f'Phone Name : {names} | Phone Price : {prices} | Phone Specifications :{Speci} | | Phone Ratings :{ratings}')

    # print(f'page {page} is done')
        names_list.append(names)
        prices_list.append(prices)
        speci_list.append(Speci)
        ratings_list.append(ratings)
    
flipkart_phones['names'] = names_list
flipkart_phones['prices'] = prices_list
flipkart_phones['specifications'] = speci_list
flipkart_phones['ratings'] = ratings_list

# print(flipkart_phones)

file = pd.DataFrame(flipkart_phones, columns = ['names', 'prices','specifications','ratings'])
# print(file)
# file.to_csv('Flipkart phones Details.csv')
        