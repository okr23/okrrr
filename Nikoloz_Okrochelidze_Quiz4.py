import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_website():
    base_url = 'https://example.com'
    page_number = 1
    delay_seconds = 15

    while True:
        url = f'{base_url}/page/{page_number}'
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error accessing page {page_number}. Skipping...")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        data = extract_data(soup)

        save_to_csv(data)

        time.sleep(delay_seconds)

        page_number += 1

def extract_data(soup):
    data = []

    article_titles = soup.find_all('h2', class_='article-title')
    for title in article_titles:
        data.append(title.text.strip())

    return data

def save_to_csv(data):
    csv_file = 'scraped_data.csv'

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

scrape_website()
