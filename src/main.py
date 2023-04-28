from export import export_data
from scraping import scrape
from summarization import summarize

URLS = [r"https://www.gov.il/he/Departments/policies?OfficeId=e744bba9-d17e-429f-abc3-50f7a8a55667&blockCollector=true&limit=10&PmoMinistersComittee=a0d9709c-f07d-4b0e-8c48-0939643eb020&skip=0",
r"https://main.knesset.gov.il/about/departments/pages/sg/sgpresidium.aspx",
r"https://main.knesset.gov.il/activity/committees/pages/allcommitteesagenda.aspx?tab=1",
r"https://www.gov.il/he/Departments/publications/?OfficeId=e744bba9-d17e-429f-abc3-50f7a8a55667&blockCollector=true&limit=10&publicationType=06311039-a4dc-4457-af46-a8e7dbfbe5a0&skip=0"]

while True:
    for url in URLS:
        scraped = scrape(url)
        analyzed = summarize(scraped)
        export_data(analyzed)
        


