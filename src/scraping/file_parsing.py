import PyPDF2

from src.common import ScrapedData


def read_pdf(pdf_path: str) -> ScrapedData:
    pdfFileObj = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    all_text = [page.extract_text() for page in pdfReader.pages]
    pdfFileObj.close()
    return ScrapedData(data=' '.join(all_text), url=pdf_path)
