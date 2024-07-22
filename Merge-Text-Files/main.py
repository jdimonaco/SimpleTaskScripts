# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.

# Import the Path class from the pathlib module for handling filesystem paths
from pathlib import Path

# Define the directory containing the files to be merged
files_dir = Path('files')

# # Initialise an empty string to store the merged content
merged = ''
for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
  merged = merged+ content + '\n'

# Open a new file (or overwrite if it exists) named 'merged.csv' in write mode
with open('merged.csv', 'w') as file:
  file.write(merged)
