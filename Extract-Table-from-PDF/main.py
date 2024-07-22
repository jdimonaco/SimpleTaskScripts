from PyPDF2 import PdfReader

reader = PdfReader('weather.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

