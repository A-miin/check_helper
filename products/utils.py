import requests
from bs4 import BeautifulSoup
from django.db.transaction import atomic

from products.models import ProductCategory, Product

main_url = "https://globus-online.kg"


def get_text_before_first_space(text):
    index = text.find(' ')
    return text[:index]


def create_category(category_html):
    print(category_html)
    category_name = category_html.find("a", class_="parent").text
    category_photo_link = main_url + category_html.find("img")["src"]
    category = ProductCategory.objects.create(name=category_name, photo_link=category_photo_link)
    return category


def create_product(product_html, category):
    price = product_html.find("span", class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text
    price = get_text_before_first_space(price)
    img = product_html.find("img")
    product_name = img['title']
    product_photo_link=main_url
    try:
        product_photo_link += img['data-src']
    except Exception:
        try:
            product_photo_link += img("img")['src']
        except Exception:
            product_photo_link += '/bitrix/templates/profood_default/assets/img/empty_198_208.png'
    product = Product.objects.create(name=product_name, photo_link=product_photo_link, category=category, price=price)
    print(product)

@atomic
def scrap_products():
    catalog_link = main_url + '/catalog'
    page = requests.get(catalog_link)

    soup = BeautifulSoup(page.content, "html.parser")
    categories = soup.find_all("li", class_="section col-xs-4 col-md-3 col-lg-5rs")
    for category in categories:
        category_url = main_url + category.find("a", class_="parent")["href"]
        category_page = requests.get(category_url)
        category_soup = BeautifulSoup(category_page.content, "html.parser")
        category_obj = create_category(category)
        products = category_soup.find_all("div", class_="list-showcase__part-main")
        for product in products:
            create_product(product, category_obj)

scrap_products()
