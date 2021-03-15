import requests
from bs4 import BeautifulSoup
import csv


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    category_file = open('CategoryList.txt', 'r')
    Lines = category_file.readlines()
    
    URL = 'https://mvnrepository.com/open-source/'

    with open('overallPackages.csv', mode='w', newline='') as csv_file:

        fieldnames = ['category', 'pkg_title', 'pkg_subtitle']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for line in Lines:
            category = line.strip()

            for x in range(1, 11):
                URL_page = URL + category + "?p=" + str(x)

                page = requests.get(URL_page)

                soup = BeautifulSoup(page.content, 'html.parser')

                pg = soup.find(id='page')

                print(soup)

                main_content = pg.find('div', id='maincontent')

                results = main_content.find_all('div', style=lambda value: value and 'padding-left:10px' in value)

                for result in results:
                    pkg_item = result.find('div', class_='im')

                    pkg_elem = pkg_item.find('div', class_='im-header')

                    title_elem = pkg_elem.find('h2', class_='im-title')
                    pkg_title = title_elem.find('a').string

                    subtitle_elem = pkg_elem.find('p', class_='im-subtitle')
                    pkg_subtitle = subtitle_elem.find('a').string

                    if None in (pkg_title, pkg_subtitle):
                        continue

                    writer.writerow({'category': category, 'pkg_title': pkg_title.strip(), 'pkg_subtitle': pkg_subtitle.strip()})
