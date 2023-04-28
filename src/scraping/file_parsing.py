import PyPDF2
import docx
import tempfile
import requests
import textract

from src.common import ScrapedData


def read_pdf(pdf_path: str) -> ScrapedData:
    pdfFileObj = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    all_text = [page.extract_text() for page in pdfReader.pages]
    pdfFileObj.close()
    return ScrapedData(data=' '.join(all_text), url=pdf_path)


def read_docx(docx_path: str) -> ScrapedData:
    # Import the python-docx library

    # Open the Hebrew Word document file with the correct encoding
    doc = docx.Document(docx_path)

    paragrphs = [para.text for para in doc.paragraphs]
    text = ' '.join(paragrphs)
    return ScrapedData(data=text, url=docx_path)

def get_text(url: str) -> ScrapedData:
    with tempfile.NamedTemporaryFile() as file_obj:
        file_obj.write(requests.get(url).content)
        if url.endswith('pdf'):
            return read_pdf(file_obj.name)
        if url.endswith('docx') or url.endswith('doc'):
            return read_docx(file_obj.name)

        
if __name__=='__main__':
    
    print(get_text(r'https://www.gov.il/BlobFolder/policy/3403m-procedure/he/forms_34.03m9.docx'))
    with open('test.txt', 'w') as f:
        x = get_text(r'https://fs.knesset.gov.il/25/Plenum/25_ptm_1344246.doc')
        f.write(x.data)
