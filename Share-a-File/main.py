# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/


# Define your Filestack API key
api_key = "YOUR API KEY"

# Initialize the Filestack client with your API key
filestack_client = Client(api_key)

# Upload the specified file and get the new link
uploaded_file = filestack_client.upload(filepath='file.txt')

# Print the URL of the uploaded file
print(uploaded_file.url)
