#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup


regex_name = 'M[0-9]{1,3}'

def get_soup():
    with open('./catalogue.html', 'r') as f:
        raw_content = f.read()
    return BeautifulSoup(raw_content, 'html.parser')

soup = get_soup()
for row in soup.find_all('tr'):
    header = row.find('th')
    cells = row.find_all('td')

    d = {}
    d['name'] = re.match(regex_name, header.text).group(0)
    d['alias'] = cells[0].text.replace('<td>', '').replace('</td>', '').strip()
    d['image_url'] = 'https:' + '/'.join(cells[2].find('img').attrs['src'].replace('thumb/', '').split('/')[:-1])
    d['otype'] = cells[3].text.strip()
    d['distance'] = cells[4].text.strip()
    d['constellation'] = cells[5].text.strip()
    d['vmag'] = cells[6].text.strip()
    d['ra'] = cells[7].text.strip()
    d['dec'] = cells[8].text.strip()

    print(d)
    print('\n')
