# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from PyPDF2 import PdfReader

reader = PdfReader('weather.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

