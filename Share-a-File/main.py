# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from filestack import Client

api_key = "AViVqp7suSQWWEdrl6hf9z"

client = Client(api_key)
new_link = client.upload(filepath='file.txt')

print(new_link.url)
