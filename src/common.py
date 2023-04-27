from dataclasses import dataclass
from datetime import datetime

from src.scraping.file_parsing import read_pdf
from src.scraping.knesset import parse_knesset


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


BE_SCRAPE_MAPPING = {"knesset": BECallable(callable_method=parse_knesset, args=[]),
                     "read from pdf": BECallable(callable_method=read_pdf, args=['pdf_path'])
                     }
# BE_SCRAPE_MAPPING[called_method].callable_method(**kwargs)
BE_ANALYZE_MAPPING = {}
