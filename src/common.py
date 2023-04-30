from dataclasses import dataclass
from datetime import datetime
from typing import List
from urllib.request import urlopen
import json
from pathlib import Path
from bs4 import BeautifulSoup

URLS = json.loads(Path("data/urls.json").read_text(encoding="UTF-8"))["urls_for_scraping"]
KEYWORDS = (Path("data") / "keywords.txt").read_text().split("\n")  # careful not to end file with blank line.

@dataclass
class ScrapedData:
    url: str
    data: str
    last_modified: datetime = datetime.now()


@dataclass
class AnalyzedData:
    data: str
    last_modified: datetime

@dataclass
class BECallable:
    callable_method: callable
    args: list
    url: str

    def parse_knesset(self) -> List[ScrapedData]:
        html = urlopen(self.url).read()
        soup = BeautifulSoup(html, features="html.parser")
        return soup



