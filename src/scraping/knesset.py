from typing import List
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.common import ScrapedData

hakika_url = 'https://www.gov.il/he/Departments/policies?OfficeId=e744bba9-d17e-429f-abc3-50f7a8a55667&blockCollector=true&limit=10&PmoMinistersComittee=a0d9709c-f07d-4b0e-8c48-0939643eb020&skip=0'
url = hakika_url


def parse_knesset() -> List[ScrapedData]:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    print(1)


if __name__ == '__main__':
    parse_knesset()
