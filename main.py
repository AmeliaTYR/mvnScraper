import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('apachePackages.csv', mode='w', newline='') as csv_file:

        fieldnames = ['pkg_title', 'pkg_subtitle']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        URL = 'https://mvnrepository.com/artifact/org.apache?p='

        for x in range(1, 11):
            URL_page = URL + str(x)

            page = requests.get(URL_page)

            soup = BeautifulSoup(page.content, 'html.parser')

            pg = soup.find(id='page')

            # print(pg)

            main_content = pg.find(id='maincontent')

            results = main_content.find_all('div', style=lambda value: value and 'padding-left:10px' in value)

            # print(results.prettify())

            for result in results:
                pkg_item = result.find('div', class_='im')

                pkg_elem = pkg_item.find('div', class_='im-header')

                title_elem = pkg_elem.find('h2', class_='im-title')
                pkg_title = title_elem.find('a').string

                subtitle_elem = pkg_elem.find('p', class_='im-subtitle')
                pkg_subtitle = subtitle_elem.find('a').string

                if None in (pkg_title, pkg_subtitle):
                    continue

                # print(pkg_title.strip())
                # print(pkg_subtitle.strip())
                # print()

                writer.writerow({'pkg_title': pkg_title.strip(), 'pkg_subtitle': pkg_subtitle.strip()})
