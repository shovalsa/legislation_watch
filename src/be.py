from dataclasses import dataclass


@dataclass
class BECallable:
    callable_method: callable
    args: list


BE_SCRAPE_MAPPING = {"knesset": BECallable(callable_method=parse_knesset, args=[]),
                     "read from pdf": BECallable(callable_method=read_pdf, args=['pdf_path']),
                     "read from website": BECallable(callable_method=scrape, args=['url'])
                     }
# BE_SCRAPE_MAPPING[called_method].callable_method(**kwargs)
BE_ANALYZE_MAPPING = {}
