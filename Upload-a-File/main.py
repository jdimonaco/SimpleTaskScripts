# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests

# URL to which the file will be uploaded
upload_url = "https://cgi-lib.berkeley.edu/ex/fup.cgi"

# Open the file in binary read mode
with open('myfile.txt', 'rb') as file_to_upload:
    # Send a POST request with the file
    response = requests.post(upload_url, files={"upfile": file_to_upload})

# Print the server's response text
print(response.text)
