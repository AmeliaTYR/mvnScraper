import requests
from bs4 import BeautifulSoup


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("CategoryList.txt", "a")

    URL = 'https://mvnrepository.com/open-source?p='

    for x in range(1, 11):
        # Find list of subsections
        URL_page = URL + str(x)

        page = requests.get(URL_page)

        soup = BeautifulSoup(page.content, 'html.parser')

        pg = soup.find(id='page')

        main_content = pg.find('div', id='maincontent')

        classToIgnore = ["breadcrumb"]
        results = main_content.find_all('div', class_=lambda x: x not in classToIgnore)

        # print(results.prettify())

        for result in results:
            cat_header = result.find('h4')

            category = cat_header.find('a').string
            # print(category.strip())

            f.write(category.strip() + "\n")

    f.close()
