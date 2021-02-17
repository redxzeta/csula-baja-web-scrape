import json
from bs4 import BeautifulSoup
from selenium import webdriver
from team import members
import os

def alumni_scrape(soup, driver):
    baja_site = soup.find('div', id="content").find_all('p')
    driver.close()
    baja_site.pop(0)
    baja_site.pop(0)
    baja_site.pop(0)
    counter = 1
    alumni_data = []
    heading = {}
    student_quotes = []
    student = {}
    quote = ""
    name = ""
    student_counter = 10
    for x in baja_site:
        y = x.get('class', '')

        if y == ['heading']:
            if student_quotes:
                a = {"students": student_quotes}
                heading.update(a)
                alumni_data.append(heading)
                student_quotes = []
            word = f"{str(x.text.strip())}"
            heading = {
                "id": counter,
                "question": word
            }
            counter += 1
        elif y == ['nameText']:
            name = (str(x.text.strip())).replace("- ", "")
        elif y == ['titleText']:
            title = str(x.text.strip())
            title = title.split(", ")
            student = {
                "id": student_counter * 10 + 5,
                "quote": quote,
                "title": title[1],
                "field": title[0],
                "name": name
            }
            student_quotes.append(student)
            student_counter += 5

        else:
            quote = f"{str(x.text.strip())}"
            quote = quote.replace('"', "")
            quote = quote.replace(u"\u00a0", " ")
    a = {"students": student_quotes}
    heading.update(a)
    alumni_data.append(heading)

    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(alumni_data, outfile, ensure_ascii=False, indent=4)


def web_scrape():
    driver = webdriver.Chrome("chromedriver.exe")
    dom = ''
    search_url = f"{os.environ.get('DOMAIN')}{dom}"
    driver.get(search_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    members(soup)
    driver.close()


if __name__ == '__main__':
    web_scrape()
