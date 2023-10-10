import requests
from bs4 import BeautifulSoup as bs
import csv
import string

# Constants
BASE_URL = "https://www.itb.ac.id/directories/listby/"
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

# Function to extract and clean text from an element
def extract_text(element):
    return element.text.strip() if element else ''

def extract_url(element):
    try:
        return element.find('a', href=True)['href']
    except:
        return ''

# Function to extract education, research, publication, and books information
def extract_info(section):
    result = []
    for h6 in section.find_all("h6", class_="font-color-04 font-weight-bold")[1:]:
        item = extract_text(h6)
        url = extract_url(h6)
        result.append([item, url])
    return result

def extract_address(section):
    address = section.find('address').text.split('\n')
    alamat, kodepos, telepon, fax, email = map(str.strip, (address[3], address[4], address[6], address[8], address[9]))
    return alamat, kodepos, telepon, fax, email

def write_csv(filename, data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ['Nama', 'URL', 'Alamat', 'Kode Pos', 'Telepon', 'Fax', 'Email']
        writer.writerow(header)
        writer.writerows(data)

def main():
    data = []
    s = requests.Session()

    for atoz in string.ascii_uppercase:
        html = s.get(BASE_URL + atoz, timeout=TIMEOUT, headers=HEADERS).content
        soup = bs(html, 'html.parser')
        for info in extract_info(soup):
            nama, url = info
            html_ = s.get(url, timeout=TIMEOUT, headers=HEADERS).content
            soup_ = bs(html_, 'html.parser')
            alamat, kodepos, telepon, fax, email = extract_address(soup_)
            row = [nama, url, alamat, kodepos, telepon, fax, email]
            if row:
                data.append(row)

    write_csv('data_directory_itb.csv', data)

if __name__ == '__main__':
    main()
