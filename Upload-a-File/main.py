# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests

url = "https://cgi-lib.berkeley.edu/ex/fup.cgi"

file = open('myfile.txt', 'rb')

req = requests.post(url, files={"upfile":file})

print(req.text)
