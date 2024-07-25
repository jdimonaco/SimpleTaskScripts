# This code is part of exercises from the Automate Everything with Python by Ardit Sulce
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

# Import the Path class from the pathlib module for handling filesystem paths
from pathlib import Path

# Specify the directory containing the files to be merged
directory = Path('files')

# Initialize a variable to store the combined content
combined_content = ''
for file_path in directory.iterdir():
    with open(file_path, 'r') as f:
        file_content = f.read()
    combined_content += file_content + '\n'

# Create (or overwrite) a file named 'merged.csv' and write the combined content to it
with open('merged.csv', 'w') as output_file:
    output_file.write(combined_content)

