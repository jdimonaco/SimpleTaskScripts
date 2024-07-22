# This code is part of exercises from the Automate Everything with Python by Ardit Sulce
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

# Import the Path class from the pathlib module to handle filesystem paths
from pathlib import Path

# Create a Path object pointing to the current directory.
root_dir = Path('.')
# Define the search term to look for in filenames
search_term = '14'

# Iterate over all files and directories 
for path in root_dir.rglob("*"):
  # Check if the current path is a file (not a directory)
  if path.is_file():
    # Check if the search term is present in the filename
    if search_term in path.stem:
      print(path.absolute())




