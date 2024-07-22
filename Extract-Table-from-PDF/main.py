# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

# Import the PdfReader class from the PyPDF2 library
from PyPDF2 import PdfReader

# Create a PdfReader object 
reader = PdfReader('weather.pdf')

# Determine the number of pages in the PDF
number_of_pages = len(reader.pages)

# Access the first page of the PDF
page = reader.pages[0]

# Extract the text from the first page
text = page.extract_text()


